"""
Type annotations for redshift-data service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_redshift_data.client import RedshiftDataAPIServiceClient
    from mypy_boto3_redshift_data.paginator import (
        DescribeTablePaginator,
        GetStatementResultPaginator,
        GetStatementResultV2Paginator,
        ListDatabasesPaginator,
        ListSchemasPaginator,
        ListStatementsPaginator,
        ListTablesPaginator,
    )

    session = Session()
    client: RedshiftDataAPIServiceClient = session.client("redshift-data")

    describe_table_paginator: DescribeTablePaginator = client.get_paginator("describe_table")
    get_statement_result_paginator: GetStatementResultPaginator = client.get_paginator("get_statement_result")
    get_statement_result_v2_paginator: GetStatementResultV2Paginator = client.get_paginator("get_statement_result_v2")
    list_databases_paginator: ListDatabasesPaginator = client.get_paginator("list_databases")
    list_schemas_paginator: ListSchemasPaginator = client.get_paginator("list_schemas")
    list_statements_paginator: ListStatementsPaginator = client.get_paginator("list_statements")
    list_tables_paginator: ListTablesPaginator = client.get_paginator("list_tables")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeTableRequestPaginateTypeDef,
    DescribeTableResponseTypeDef,
    GetStatementResultRequestPaginateTypeDef,
    GetStatementResultResponseTypeDef,
    GetStatementResultV2RequestPaginateTypeDef,
    GetStatementResultV2ResponseTypeDef,
    ListDatabasesRequestPaginateTypeDef,
    ListDatabasesResponseTypeDef,
    ListSchemasRequestPaginateTypeDef,
    ListSchemasResponseTypeDef,
    ListStatementsRequestPaginateTypeDef,
    ListStatementsResponseTypeDef,
    ListTablesRequestPaginateTypeDef,
    ListTablesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeTablePaginator",
    "GetStatementResultPaginator",
    "GetStatementResultV2Paginator",
    "ListDatabasesPaginator",
    "ListSchemasPaginator",
    "ListStatementsPaginator",
    "ListTablesPaginator",
)

if TYPE_CHECKING:
    _DescribeTablePaginatorBase = Paginator[DescribeTableResponseTypeDef]
else:
    _DescribeTablePaginatorBase = Paginator  # type: ignore[assignment]

class DescribeTablePaginator(_DescribeTablePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/paginator/DescribeTable.html#RedshiftDataAPIService.Paginator.DescribeTable)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/paginators/#describetablepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTableRequestPaginateTypeDef]
    ) -> PageIterator[DescribeTableResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/paginator/DescribeTable.html#RedshiftDataAPIService.Paginator.DescribeTable.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/paginators/#describetablepaginator)
        """

if TYPE_CHECKING:
    _GetStatementResultPaginatorBase = Paginator[GetStatementResultResponseTypeDef]
else:
    _GetStatementResultPaginatorBase = Paginator  # type: ignore[assignment]

class GetStatementResultPaginator(_GetStatementResultPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/paginator/GetStatementResult.html#RedshiftDataAPIService.Paginator.GetStatementResult)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/paginators/#getstatementresultpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetStatementResultRequestPaginateTypeDef]
    ) -> PageIterator[GetStatementResultResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/paginator/GetStatementResult.html#RedshiftDataAPIService.Paginator.GetStatementResult.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/paginators/#getstatementresultpaginator)
        """

if TYPE_CHECKING:
    _GetStatementResultV2PaginatorBase = Paginator[GetStatementResultV2ResponseTypeDef]
else:
    _GetStatementResultV2PaginatorBase = Paginator  # type: ignore[assignment]

class GetStatementResultV2Paginator(_GetStatementResultV2PaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/paginator/GetStatementResultV2.html#RedshiftDataAPIService.Paginator.GetStatementResultV2)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/paginators/#getstatementresultv2paginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetStatementResultV2RequestPaginateTypeDef]
    ) -> PageIterator[GetStatementResultV2ResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/paginator/GetStatementResultV2.html#RedshiftDataAPIService.Paginator.GetStatementResultV2.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/paginators/#getstatementresultv2paginator)
        """

if TYPE_CHECKING:
    _ListDatabasesPaginatorBase = Paginator[ListDatabasesResponseTypeDef]
else:
    _ListDatabasesPaginatorBase = Paginator  # type: ignore[assignment]

class ListDatabasesPaginator(_ListDatabasesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/paginator/ListDatabases.html#RedshiftDataAPIService.Paginator.ListDatabases)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/paginators/#listdatabasespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDatabasesRequestPaginateTypeDef]
    ) -> PageIterator[ListDatabasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/paginator/ListDatabases.html#RedshiftDataAPIService.Paginator.ListDatabases.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/paginators/#listdatabasespaginator)
        """

if TYPE_CHECKING:
    _ListSchemasPaginatorBase = Paginator[ListSchemasResponseTypeDef]
else:
    _ListSchemasPaginatorBase = Paginator  # type: ignore[assignment]

class ListSchemasPaginator(_ListSchemasPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/paginator/ListSchemas.html#RedshiftDataAPIService.Paginator.ListSchemas)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/paginators/#listschemaspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSchemasRequestPaginateTypeDef]
    ) -> PageIterator[ListSchemasResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/paginator/ListSchemas.html#RedshiftDataAPIService.Paginator.ListSchemas.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/paginators/#listschemaspaginator)
        """

if TYPE_CHECKING:
    _ListStatementsPaginatorBase = Paginator[ListStatementsResponseTypeDef]
else:
    _ListStatementsPaginatorBase = Paginator  # type: ignore[assignment]

class ListStatementsPaginator(_ListStatementsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/paginator/ListStatements.html#RedshiftDataAPIService.Paginator.ListStatements)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/paginators/#liststatementspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListStatementsRequestPaginateTypeDef]
    ) -> PageIterator[ListStatementsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/paginator/ListStatements.html#RedshiftDataAPIService.Paginator.ListStatements.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/paginators/#liststatementspaginator)
        """

if TYPE_CHECKING:
    _ListTablesPaginatorBase = Paginator[ListTablesResponseTypeDef]
else:
    _ListTablesPaginatorBase = Paginator  # type: ignore[assignment]

class ListTablesPaginator(_ListTablesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/paginator/ListTables.html#RedshiftDataAPIService.Paginator.ListTables)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/paginators/#listtablespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTablesRequestPaginateTypeDef]
    ) -> PageIterator[ListTablesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data/paginator/ListTables.html#RedshiftDataAPIService.Paginator.ListTables.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/paginators/#listtablespaginator)
        """
