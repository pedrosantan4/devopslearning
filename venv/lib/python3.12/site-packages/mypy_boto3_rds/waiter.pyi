"""
Type annotations for rds service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_rds.client import RDSClient
    from mypy_boto3_rds.waiter import (
        DBClusterAvailableWaiter,
        DBClusterDeletedWaiter,
        DBClusterSnapshotAvailableWaiter,
        DBClusterSnapshotDeletedWaiter,
        DBInstanceAvailableWaiter,
        DBInstanceDeletedWaiter,
        DBSnapshotAvailableWaiter,
        DBSnapshotCompletedWaiter,
        DBSnapshotDeletedWaiter,
        TenantDatabaseAvailableWaiter,
        TenantDatabaseDeletedWaiter,
    )

    session = Session()
    client: RDSClient = session.client("rds")

    db_cluster_available_waiter: DBClusterAvailableWaiter = client.get_waiter("db_cluster_available")
    db_cluster_deleted_waiter: DBClusterDeletedWaiter = client.get_waiter("db_cluster_deleted")
    db_cluster_snapshot_available_waiter: DBClusterSnapshotAvailableWaiter = client.get_waiter("db_cluster_snapshot_available")
    db_cluster_snapshot_deleted_waiter: DBClusterSnapshotDeletedWaiter = client.get_waiter("db_cluster_snapshot_deleted")
    db_instance_available_waiter: DBInstanceAvailableWaiter = client.get_waiter("db_instance_available")
    db_instance_deleted_waiter: DBInstanceDeletedWaiter = client.get_waiter("db_instance_deleted")
    db_snapshot_available_waiter: DBSnapshotAvailableWaiter = client.get_waiter("db_snapshot_available")
    db_snapshot_completed_waiter: DBSnapshotCompletedWaiter = client.get_waiter("db_snapshot_completed")
    db_snapshot_deleted_waiter: DBSnapshotDeletedWaiter = client.get_waiter("db_snapshot_deleted")
    tenant_database_available_waiter: TenantDatabaseAvailableWaiter = client.get_waiter("tenant_database_available")
    tenant_database_deleted_waiter: TenantDatabaseDeletedWaiter = client.get_waiter("tenant_database_deleted")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import (
    DescribeDBClustersMessageWaitExtraTypeDef,
    DescribeDBClustersMessageWaitTypeDef,
    DescribeDBClusterSnapshotsMessageWaitExtraTypeDef,
    DescribeDBClusterSnapshotsMessageWaitTypeDef,
    DescribeDBInstancesMessageWaitExtraTypeDef,
    DescribeDBInstancesMessageWaitTypeDef,
    DescribeDBSnapshotsMessageWaitExtraExtraTypeDef,
    DescribeDBSnapshotsMessageWaitExtraTypeDef,
    DescribeDBSnapshotsMessageWaitTypeDef,
    DescribeTenantDatabasesMessageWaitExtraTypeDef,
    DescribeTenantDatabasesMessageWaitTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DBClusterAvailableWaiter",
    "DBClusterDeletedWaiter",
    "DBClusterSnapshotAvailableWaiter",
    "DBClusterSnapshotDeletedWaiter",
    "DBInstanceAvailableWaiter",
    "DBInstanceDeletedWaiter",
    "DBSnapshotAvailableWaiter",
    "DBSnapshotCompletedWaiter",
    "DBSnapshotDeletedWaiter",
    "TenantDatabaseAvailableWaiter",
    "TenantDatabaseDeletedWaiter",
)

class DBClusterAvailableWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/waiter/DBClusterAvailable.html#RDS.Waiter.DBClusterAvailable)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters/#dbclusteravailablewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBClustersMessageWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/waiter/DBClusterAvailable.html#RDS.Waiter.DBClusterAvailable.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters/#dbclusteravailablewaiter)
        """

class DBClusterDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/waiter/DBClusterDeleted.html#RDS.Waiter.DBClusterDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters/#dbclusterdeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBClustersMessageWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/waiter/DBClusterDeleted.html#RDS.Waiter.DBClusterDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters/#dbclusterdeletedwaiter)
        """

class DBClusterSnapshotAvailableWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/waiter/DBClusterSnapshotAvailable.html#RDS.Waiter.DBClusterSnapshotAvailable)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters/#dbclustersnapshotavailablewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBClusterSnapshotsMessageWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/waiter/DBClusterSnapshotAvailable.html#RDS.Waiter.DBClusterSnapshotAvailable.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters/#dbclustersnapshotavailablewaiter)
        """

class DBClusterSnapshotDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/waiter/DBClusterSnapshotDeleted.html#RDS.Waiter.DBClusterSnapshotDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters/#dbclustersnapshotdeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBClusterSnapshotsMessageWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/waiter/DBClusterSnapshotDeleted.html#RDS.Waiter.DBClusterSnapshotDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters/#dbclustersnapshotdeletedwaiter)
        """

class DBInstanceAvailableWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/waiter/DBInstanceAvailable.html#RDS.Waiter.DBInstanceAvailable)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters/#dbinstanceavailablewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBInstancesMessageWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/waiter/DBInstanceAvailable.html#RDS.Waiter.DBInstanceAvailable.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters/#dbinstanceavailablewaiter)
        """

class DBInstanceDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/waiter/DBInstanceDeleted.html#RDS.Waiter.DBInstanceDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters/#dbinstancedeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBInstancesMessageWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/waiter/DBInstanceDeleted.html#RDS.Waiter.DBInstanceDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters/#dbinstancedeletedwaiter)
        """

class DBSnapshotAvailableWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/waiter/DBSnapshotAvailable.html#RDS.Waiter.DBSnapshotAvailable)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters/#dbsnapshotavailablewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBSnapshotsMessageWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/waiter/DBSnapshotAvailable.html#RDS.Waiter.DBSnapshotAvailable.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters/#dbsnapshotavailablewaiter)
        """

class DBSnapshotCompletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/waiter/DBSnapshotCompleted.html#RDS.Waiter.DBSnapshotCompleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters/#dbsnapshotcompletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBSnapshotsMessageWaitExtraExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/waiter/DBSnapshotCompleted.html#RDS.Waiter.DBSnapshotCompleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters/#dbsnapshotcompletedwaiter)
        """

class DBSnapshotDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/waiter/DBSnapshotDeleted.html#RDS.Waiter.DBSnapshotDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters/#dbsnapshotdeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBSnapshotsMessageWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/waiter/DBSnapshotDeleted.html#RDS.Waiter.DBSnapshotDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters/#dbsnapshotdeletedwaiter)
        """

class TenantDatabaseAvailableWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/waiter/TenantDatabaseAvailable.html#RDS.Waiter.TenantDatabaseAvailable)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters/#tenantdatabaseavailablewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTenantDatabasesMessageWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/waiter/TenantDatabaseAvailable.html#RDS.Waiter.TenantDatabaseAvailable.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters/#tenantdatabaseavailablewaiter)
        """

class TenantDatabaseDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/waiter/TenantDatabaseDeleted.html#RDS.Waiter.TenantDatabaseDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters/#tenantdatabasedeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTenantDatabasesMessageWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/waiter/TenantDatabaseDeleted.html#RDS.Waiter.TenantDatabaseDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters/#tenantdatabasedeletedwaiter)
        """
