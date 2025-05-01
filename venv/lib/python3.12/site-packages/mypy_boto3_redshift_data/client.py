"""
Type annotations for redshift-data service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_redshift_data.client import RedshiftDataAPIServiceClient

    session = Session()
    client: RedshiftDataAPIServiceClient = session.client("redshift-data")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    DescribeTablePaginator,
    GetStatementResultPaginator,
    GetStatementResultV2Paginator,
    ListDatabasesPaginator,
    ListSchemasPaginator,
    ListStatementsPaginator,
    ListTablesPaginator,
)
from .type_defs import (
    BatchExecuteStatementInputTypeDef,
    BatchExecuteStatementOutputTypeDef,
    CancelStatementRequestTypeDef,
    CancelStatementResponseTypeDef,
    DescribeStatementRequestTypeDef,
    DescribeStatementResponseTypeDef,
    DescribeTableRequestTypeDef,
    DescribeTableResponseTypeDef,
    ExecuteStatementInputTypeDef,
    ExecuteStatementOutputTypeDef,
    GetStatementResultRequestTypeDef,
    GetStatementResultResponseTypeDef,
    GetStatementResultV2RequestTypeDef,
    GetStatementResultV2ResponseTypeDef,
    ListDatabasesRequestTypeDef,
    ListDatabasesResponseTypeDef,
    ListSchemasRequestTypeDef,
    ListSchemasResponseTypeDef,
    ListStatementsRequestTypeDef,
    ListStatementsResponseTypeDef,
    ListTablesRequestTypeDef,
    ListTablesResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack


__all__ = ("RedshiftDataAPIServiceClient",)


class Exceptions(BaseClientExceptions):
    ActiveSessionsExceededException: Type[BotocoreClientError]
    ActiveStatementsExceededException: Type[BotocoreClientError]
    BatchExecuteStatementException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DatabaseConnectionException: Type[BotocoreClientError]
    ExecuteStatementException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    QueryTimeoutException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class RedshiftDataAPIServiceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        RedshiftDataAPIServiceClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html#RedshiftDataAPIService.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#generate_presigned_url)
        """

    def batch_execute_statement(
        self, **kwargs: Unpack[BatchExecuteStatementInputTypeDef]
    ) -> BatchExecuteStatementOutputTypeDef:
        """
        Runs one or more SQL statements, which can be data manipulation language (DML)
        or data definition language (DDL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/client/batch_execute_statement.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#batch_execute_statement)
        """

    def cancel_statement(
        self, **kwargs: Unpack[CancelStatementRequestTypeDef]
    ) -> CancelStatementResponseTypeDef:
        """
        Cancels a running query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/client/cancel_statement.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#cancel_statement)
        """

    def describe_statement(
        self, **kwargs: Unpack[DescribeStatementRequestTypeDef]
    ) -> DescribeStatementResponseTypeDef:
        """
        Describes the details about a specific instance when a query was run by the
        Amazon Redshift Data API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/client/describe_statement.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#describe_statement)
        """

    def describe_table(
        self, **kwargs: Unpack[DescribeTableRequestTypeDef]
    ) -> DescribeTableResponseTypeDef:
        """
        Describes the detailed information about a table from metadata in the cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/client/describe_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#describe_table)
        """

    def execute_statement(
        self, **kwargs: Unpack[ExecuteStatementInputTypeDef]
    ) -> ExecuteStatementOutputTypeDef:
        """
        Runs an SQL statement, which can be data manipulation language (DML) or data
        definition language (DDL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/client/execute_statement.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#execute_statement)
        """

    def get_statement_result(
        self, **kwargs: Unpack[GetStatementResultRequestTypeDef]
    ) -> GetStatementResultResponseTypeDef:
        """
        Fetches the temporarily cached result of an SQL statement in JSON format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/client/get_statement_result.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#get_statement_result)
        """

    def get_statement_result_v2(
        self, **kwargs: Unpack[GetStatementResultV2RequestTypeDef]
    ) -> GetStatementResultV2ResponseTypeDef:
        """
        Fetches the temporarily cached result of an SQL statement in CSV format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/client/get_statement_result_v2.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#get_statement_result_v2)
        """

    def list_databases(
        self, **kwargs: Unpack[ListDatabasesRequestTypeDef]
    ) -> ListDatabasesResponseTypeDef:
        """
        List the databases in a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/client/list_databases.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#list_databases)
        """

    def list_schemas(
        self, **kwargs: Unpack[ListSchemasRequestTypeDef]
    ) -> ListSchemasResponseTypeDef:
        """
        Lists the schemas in a database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/client/list_schemas.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#list_schemas)
        """

    def list_statements(
        self, **kwargs: Unpack[ListStatementsRequestTypeDef]
    ) -> ListStatementsResponseTypeDef:
        """
        List of SQL statements.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/client/list_statements.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#list_statements)
        """

    def list_tables(self, **kwargs: Unpack[ListTablesRequestTypeDef]) -> ListTablesResponseTypeDef:
        """
        List the tables in a database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/client/list_tables.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#list_tables)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_table"]
    ) -> DescribeTablePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_statement_result"]
    ) -> GetStatementResultPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_statement_result_v2"]
    ) -> GetStatementResultV2Paginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_databases"]
    ) -> ListDatabasesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_schemas"]
    ) -> ListSchemasPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_statements"]
    ) -> ListStatementsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_tables"]
    ) -> ListTablesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client/#get_paginator)
        """
