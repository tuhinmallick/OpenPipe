import { type z } from "zod";
import { type Expression, type SqlBool, sql } from "kysely";

import { kysely } from "~/server/db";
import { LoggedCallsFiltersDefaultFields, type filtersSchema } from "~/types/shared.types";
import {
  textComparatorToSqlExpression,
  dateComparatorToSqlExpression,
} from "./comparatorToSqlExpression";

export const constructLoggedCallFiltersQuery = (
  filters: z.infer<typeof filtersSchema>,
  projectId: string,
  selectionParams?: {
    defaultToSelected: boolean;
    selectedLogIds: string[];
    deselectedLogIds: string[];
  },
) => {
  const baseQuery = kysely
    .selectFrom("LoggedCall as lc")
    .leftJoin("LoggedCallModelResponse as lcmr", "lc.id", "lcmr.originalLoggedCallId")
    .where((eb) => {
      const wheres: Expression<SqlBool>[] = [eb("lc.projectId", "=", projectId)];

      const dateFilters = filters.filter(
        (filter) => filter.field === LoggedCallsFiltersDefaultFields.SentAt,
      );

      // Add date-related filters first
      for (const filter of dateFilters) {
        const filterExpression = dateComparatorToSqlExpression(
          filter.comparator,
          filter.value as [number, number],
        );

        if (filter.field === LoggedCallsFiltersDefaultFields.SentAt) {
          wheres.push(filterExpression(sql.raw(`lc."requestedAt"`)));
        }
      }

      for (const filter of filters) {
        if (!filter.value) continue;
        const filterExpression = textComparatorToSqlExpression(
          filter.comparator,
          filter.value as string,
        );

        if (filter.field === LoggedCallsFiltersDefaultFields.Request) {
          wheres.push(filterExpression(sql.raw(`lcmr."reqPayload"::text`)));
        }
        if (filter.field === LoggedCallsFiltersDefaultFields.Response) {
          wheres.push(filterExpression(sql.raw(`lcmr."respPayload"::text`)));
        }
        if (filter.field === LoggedCallsFiltersDefaultFields.Model) {
          wheres.push(filterExpression(sql.raw(`lc."model"`)));
        }
        if (filter.field === LoggedCallsFiltersDefaultFields.StatusCode) {
          wheres.push(filterExpression(sql.raw(`lcmr."statusCode"::text`)));
        }
      }

      return eb.and(wheres);
    });

  const tagFilters = filters.filter(
    (filter) =>
      !Object.values(LoggedCallsFiltersDefaultFields).includes(
        filter.field as LoggedCallsFiltersDefaultFields,
      ),
  );

  let updatedBaseQuery = baseQuery;

  for (let i = 0; i < tagFilters.length; i++) {
    const filter = tagFilters[i];
    if (!filter?.value) continue;
    const tableAlias = `lct${i}`;
    const filterExpression = textComparatorToSqlExpression(
      filter.comparator,
      filter.value as string,
    );

    updatedBaseQuery = updatedBaseQuery
      .leftJoin(`LoggedCallTag as ${tableAlias}`, (join) =>
        join
          .onRef("lc.id", "=", `${tableAlias}.loggedCallId`)
          .on(`${tableAlias}.name`, "=", filter.field),
      )
      .where(filterExpression(sql.raw(`${tableAlias}.value`))) as unknown as typeof baseQuery;
  }

  if (selectionParams) {
    if (selectionParams.defaultToSelected && selectionParams.deselectedLogIds.length) {
      updatedBaseQuery = updatedBaseQuery.where(({ eb, not }) =>
        not(eb("lc.id", "in", selectionParams.deselectedLogIds)),
      );
    } else if (!selectionParams.defaultToSelected && selectionParams.selectedLogIds.length) {
      updatedBaseQuery = updatedBaseQuery.where((eb) =>
        eb("lc.id", "in", selectionParams.selectedLogIds),
      );
    }
    updatedBaseQuery = updatedBaseQuery.where((eb) => eb("lcmr.statusCode", "=", 200));
  }

  return updatedBaseQuery;
};
