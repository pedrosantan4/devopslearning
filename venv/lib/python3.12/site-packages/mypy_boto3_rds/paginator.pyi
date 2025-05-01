"""
Type annotations for rds service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_rds.client import RDSClient
    from mypy_boto3_rds.paginator import (
        DescribeBlueGreenDeploymentsPaginator,
        DescribeCertificatesPaginator,
        DescribeDBClusterAutomatedBackupsPaginator,
        DescribeDBClusterBacktracksPaginator,
        DescribeDBClusterEndpointsPaginator,
        DescribeDBClusterParameterGroupsPaginator,
        DescribeDBClusterParametersPaginator,
        DescribeDBClusterSnapshotsPaginator,
        DescribeDBClustersPaginator,
        DescribeDBEngineVersionsPaginator,
        DescribeDBInstanceAutomatedBackupsPaginator,
        DescribeDBInstancesPaginator,
        DescribeDBLogFilesPaginator,
        DescribeDBParameterGroupsPaginator,
        DescribeDBParametersPaginator,
        DescribeDBProxiesPaginator,
        DescribeDBProxyEndpointsPaginator,
        DescribeDBProxyTargetGroupsPaginator,
        DescribeDBProxyTargetsPaginator,
        DescribeDBRecommendationsPaginator,
        DescribeDBSecurityGroupsPaginator,
        DescribeDBSnapshotTenantDatabasesPaginator,
        DescribeDBSnapshotsPaginator,
        DescribeDBSubnetGroupsPaginator,
        DescribeEngineDefaultClusterParametersPaginator,
        DescribeEngineDefaultParametersPaginator,
        DescribeEventSubscriptionsPaginator,
        DescribeEventsPaginator,
        DescribeExportTasksPaginator,
        DescribeGlobalClustersPaginator,
        DescribeIntegrationsPaginator,
        DescribeOptionGroupOptionsPaginator,
        DescribeOptionGroupsPaginator,
        DescribeOrderableDBInstanceOptionsPaginator,
        DescribePendingMaintenanceActionsPaginator,
        DescribeReservedDBInstancesOfferingsPaginator,
        DescribeReservedDBInstancesPaginator,
        DescribeSourceRegionsPaginator,
        DescribeTenantDatabasesPaginator,
        DownloadDBLogFilePortionPaginator,
    )

    session = Session()
    client: RDSClient = session.client("rds")

    describe_blue_green_deployments_paginator: DescribeBlueGreenDeploymentsPaginator = client.get_paginator("describe_blue_green_deployments")
    describe_certificates_paginator: DescribeCertificatesPaginator = client.get_paginator("describe_certificates")
    describe_db_cluster_automated_backups_paginator: DescribeDBClusterAutomatedBackupsPaginator = client.get_paginator("describe_db_cluster_automated_backups")
    describe_db_cluster_backtracks_paginator: DescribeDBClusterBacktracksPaginator = client.get_paginator("describe_db_cluster_backtracks")
    describe_db_cluster_endpoints_paginator: DescribeDBClusterEndpointsPaginator = client.get_paginator("describe_db_cluster_endpoints")
    describe_db_cluster_parameter_groups_paginator: DescribeDBClusterParameterGroupsPaginator = client.get_paginator("describe_db_cluster_parameter_groups")
    describe_db_cluster_parameters_paginator: DescribeDBClusterParametersPaginator = client.get_paginator("describe_db_cluster_parameters")
    describe_db_cluster_snapshots_paginator: DescribeDBClusterSnapshotsPaginator = client.get_paginator("describe_db_cluster_snapshots")
    describe_db_clusters_paginator: DescribeDBClustersPaginator = client.get_paginator("describe_db_clusters")
    describe_db_engine_versions_paginator: DescribeDBEngineVersionsPaginator = client.get_paginator("describe_db_engine_versions")
    describe_db_instance_automated_backups_paginator: DescribeDBInstanceAutomatedBackupsPaginator = client.get_paginator("describe_db_instance_automated_backups")
    describe_db_instances_paginator: DescribeDBInstancesPaginator = client.get_paginator("describe_db_instances")
    describe_db_log_files_paginator: DescribeDBLogFilesPaginator = client.get_paginator("describe_db_log_files")
    describe_db_parameter_groups_paginator: DescribeDBParameterGroupsPaginator = client.get_paginator("describe_db_parameter_groups")
    describe_db_parameters_paginator: DescribeDBParametersPaginator = client.get_paginator("describe_db_parameters")
    describe_db_proxies_paginator: DescribeDBProxiesPaginator = client.get_paginator("describe_db_proxies")
    describe_db_proxy_endpoints_paginator: DescribeDBProxyEndpointsPaginator = client.get_paginator("describe_db_proxy_endpoints")
    describe_db_proxy_target_groups_paginator: DescribeDBProxyTargetGroupsPaginator = client.get_paginator("describe_db_proxy_target_groups")
    describe_db_proxy_targets_paginator: DescribeDBProxyTargetsPaginator = client.get_paginator("describe_db_proxy_targets")
    describe_db_recommendations_paginator: DescribeDBRecommendationsPaginator = client.get_paginator("describe_db_recommendations")
    describe_db_security_groups_paginator: DescribeDBSecurityGroupsPaginator = client.get_paginator("describe_db_security_groups")
    describe_db_snapshot_tenant_databases_paginator: DescribeDBSnapshotTenantDatabasesPaginator = client.get_paginator("describe_db_snapshot_tenant_databases")
    describe_db_snapshots_paginator: DescribeDBSnapshotsPaginator = client.get_paginator("describe_db_snapshots")
    describe_db_subnet_groups_paginator: DescribeDBSubnetGroupsPaginator = client.get_paginator("describe_db_subnet_groups")
    describe_engine_default_cluster_parameters_paginator: DescribeEngineDefaultClusterParametersPaginator = client.get_paginator("describe_engine_default_cluster_parameters")
    describe_engine_default_parameters_paginator: DescribeEngineDefaultParametersPaginator = client.get_paginator("describe_engine_default_parameters")
    describe_event_subscriptions_paginator: DescribeEventSubscriptionsPaginator = client.get_paginator("describe_event_subscriptions")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
    describe_export_tasks_paginator: DescribeExportTasksPaginator = client.get_paginator("describe_export_tasks")
    describe_global_clusters_paginator: DescribeGlobalClustersPaginator = client.get_paginator("describe_global_clusters")
    describe_integrations_paginator: DescribeIntegrationsPaginator = client.get_paginator("describe_integrations")
    describe_option_group_options_paginator: DescribeOptionGroupOptionsPaginator = client.get_paginator("describe_option_group_options")
    describe_option_groups_paginator: DescribeOptionGroupsPaginator = client.get_paginator("describe_option_groups")
    describe_orderable_db_instance_options_paginator: DescribeOrderableDBInstanceOptionsPaginator = client.get_paginator("describe_orderable_db_instance_options")
    describe_pending_maintenance_actions_paginator: DescribePendingMaintenanceActionsPaginator = client.get_paginator("describe_pending_maintenance_actions")
    describe_reserved_db_instances_offerings_paginator: DescribeReservedDBInstancesOfferingsPaginator = client.get_paginator("describe_reserved_db_instances_offerings")
    describe_reserved_db_instances_paginator: DescribeReservedDBInstancesPaginator = client.get_paginator("describe_reserved_db_instances")
    describe_source_regions_paginator: DescribeSourceRegionsPaginator = client.get_paginator("describe_source_regions")
    describe_tenant_databases_paginator: DescribeTenantDatabasesPaginator = client.get_paginator("describe_tenant_databases")
    download_db_log_file_portion_paginator: DownloadDBLogFilePortionPaginator = client.get_paginator("download_db_log_file_portion")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    CertificateMessageTypeDef,
    DBClusterAutomatedBackupMessageTypeDef,
    DBClusterBacktrackMessageTypeDef,
    DBClusterEndpointMessageTypeDef,
    DBClusterMessageTypeDef,
    DBClusterParameterGroupDetailsTypeDef,
    DBClusterParameterGroupsMessageTypeDef,
    DBClusterSnapshotMessageTypeDef,
    DBEngineVersionMessageTypeDef,
    DBInstanceAutomatedBackupMessageTypeDef,
    DBInstanceMessageTypeDef,
    DBParameterGroupDetailsTypeDef,
    DBParameterGroupsMessageTypeDef,
    DBRecommendationsMessageTypeDef,
    DBSecurityGroupMessageTypeDef,
    DBSnapshotMessageTypeDef,
    DBSnapshotTenantDatabasesMessageTypeDef,
    DBSubnetGroupMessageTypeDef,
    DescribeBlueGreenDeploymentsRequestPaginateTypeDef,
    DescribeBlueGreenDeploymentsResponseTypeDef,
    DescribeCertificatesMessagePaginateTypeDef,
    DescribeDBClusterAutomatedBackupsMessagePaginateTypeDef,
    DescribeDBClusterBacktracksMessagePaginateTypeDef,
    DescribeDBClusterEndpointsMessagePaginateTypeDef,
    DescribeDBClusterParameterGroupsMessagePaginateTypeDef,
    DescribeDBClusterParametersMessagePaginateTypeDef,
    DescribeDBClustersMessagePaginateTypeDef,
    DescribeDBClusterSnapshotsMessagePaginateTypeDef,
    DescribeDBEngineVersionsMessagePaginateTypeDef,
    DescribeDBInstanceAutomatedBackupsMessagePaginateTypeDef,
    DescribeDBInstancesMessagePaginateTypeDef,
    DescribeDBLogFilesMessagePaginateTypeDef,
    DescribeDBLogFilesResponseTypeDef,
    DescribeDBParameterGroupsMessagePaginateTypeDef,
    DescribeDBParametersMessagePaginateTypeDef,
    DescribeDBProxiesRequestPaginateTypeDef,
    DescribeDBProxiesResponseTypeDef,
    DescribeDBProxyEndpointsRequestPaginateTypeDef,
    DescribeDBProxyEndpointsResponseTypeDef,
    DescribeDBProxyTargetGroupsRequestPaginateTypeDef,
    DescribeDBProxyTargetGroupsResponseTypeDef,
    DescribeDBProxyTargetsRequestPaginateTypeDef,
    DescribeDBProxyTargetsResponseTypeDef,
    DescribeDBRecommendationsMessagePaginateTypeDef,
    DescribeDBSecurityGroupsMessagePaginateTypeDef,
    DescribeDBSnapshotsMessagePaginateTypeDef,
    DescribeDBSnapshotTenantDatabasesMessagePaginateTypeDef,
    DescribeDBSubnetGroupsMessagePaginateTypeDef,
    DescribeEngineDefaultClusterParametersMessagePaginateTypeDef,
    DescribeEngineDefaultClusterParametersResultTypeDef,
    DescribeEngineDefaultParametersMessagePaginateTypeDef,
    DescribeEngineDefaultParametersResultTypeDef,
    DescribeEventsMessagePaginateTypeDef,
    DescribeEventSubscriptionsMessagePaginateTypeDef,
    DescribeExportTasksMessagePaginateTypeDef,
    DescribeGlobalClustersMessagePaginateTypeDef,
    DescribeIntegrationsMessagePaginateTypeDef,
    DescribeIntegrationsResponseTypeDef,
    DescribeOptionGroupOptionsMessagePaginateTypeDef,
    DescribeOptionGroupsMessagePaginateTypeDef,
    DescribeOrderableDBInstanceOptionsMessagePaginateTypeDef,
    DescribePendingMaintenanceActionsMessagePaginateTypeDef,
    DescribeReservedDBInstancesMessagePaginateTypeDef,
    DescribeReservedDBInstancesOfferingsMessagePaginateTypeDef,
    DescribeSourceRegionsMessagePaginateTypeDef,
    DescribeTenantDatabasesMessagePaginateTypeDef,
    DownloadDBLogFilePortionDetailsTypeDef,
    DownloadDBLogFilePortionMessagePaginateTypeDef,
    EventsMessageTypeDef,
    EventSubscriptionsMessageTypeDef,
    ExportTasksMessageTypeDef,
    GlobalClustersMessageTypeDef,
    OptionGroupOptionsMessageTypeDef,
    OptionGroupsTypeDef,
    OrderableDBInstanceOptionsMessageTypeDef,
    PendingMaintenanceActionsMessageTypeDef,
    ReservedDBInstanceMessageTypeDef,
    ReservedDBInstancesOfferingMessageTypeDef,
    SourceRegionMessageTypeDef,
    TenantDatabasesMessageTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeBlueGreenDeploymentsPaginator",
    "DescribeCertificatesPaginator",
    "DescribeDBClusterAutomatedBackupsPaginator",
    "DescribeDBClusterBacktracksPaginator",
    "DescribeDBClusterEndpointsPaginator",
    "DescribeDBClusterParameterGroupsPaginator",
    "DescribeDBClusterParametersPaginator",
    "DescribeDBClusterSnapshotsPaginator",
    "DescribeDBClustersPaginator",
    "DescribeDBEngineVersionsPaginator",
    "DescribeDBInstanceAutomatedBackupsPaginator",
    "DescribeDBInstancesPaginator",
    "DescribeDBLogFilesPaginator",
    "DescribeDBParameterGroupsPaginator",
    "DescribeDBParametersPaginator",
    "DescribeDBProxiesPaginator",
    "DescribeDBProxyEndpointsPaginator",
    "DescribeDBProxyTargetGroupsPaginator",
    "DescribeDBProxyTargetsPaginator",
    "DescribeDBRecommendationsPaginator",
    "DescribeDBSecurityGroupsPaginator",
    "DescribeDBSnapshotTenantDatabasesPaginator",
    "DescribeDBSnapshotsPaginator",
    "DescribeDBSubnetGroupsPaginator",
    "DescribeEngineDefaultClusterParametersPaginator",
    "DescribeEngineDefaultParametersPaginator",
    "DescribeEventSubscriptionsPaginator",
    "DescribeEventsPaginator",
    "DescribeExportTasksPaginator",
    "DescribeGlobalClustersPaginator",
    "DescribeIntegrationsPaginator",
    "DescribeOptionGroupOptionsPaginator",
    "DescribeOptionGroupsPaginator",
    "DescribeOrderableDBInstanceOptionsPaginator",
    "DescribePendingMaintenanceActionsPaginator",
    "DescribeReservedDBInstancesOfferingsPaginator",
    "DescribeReservedDBInstancesPaginator",
    "DescribeSourceRegionsPaginator",
    "DescribeTenantDatabasesPaginator",
    "DownloadDBLogFilePortionPaginator",
)

if TYPE_CHECKING:
    _DescribeBlueGreenDeploymentsPaginatorBase = Paginator[
        DescribeBlueGreenDeploymentsResponseTypeDef
    ]
else:
    _DescribeBlueGreenDeploymentsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeBlueGreenDeploymentsPaginator(_DescribeBlueGreenDeploymentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeBlueGreenDeployments.html#RDS.Paginator.DescribeBlueGreenDeployments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describebluegreendeploymentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeBlueGreenDeploymentsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeBlueGreenDeploymentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeBlueGreenDeployments.html#RDS.Paginator.DescribeBlueGreenDeployments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describebluegreendeploymentspaginator)
        """

if TYPE_CHECKING:
    _DescribeCertificatesPaginatorBase = Paginator[CertificateMessageTypeDef]
else:
    _DescribeCertificatesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeCertificatesPaginator(_DescribeCertificatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeCertificates.html#RDS.Paginator.DescribeCertificates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describecertificatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeCertificatesMessagePaginateTypeDef]
    ) -> PageIterator[CertificateMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeCertificates.html#RDS.Paginator.DescribeCertificates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describecertificatespaginator)
        """

if TYPE_CHECKING:
    _DescribeDBClusterAutomatedBackupsPaginatorBase = Paginator[
        DBClusterAutomatedBackupMessageTypeDef
    ]
else:
    _DescribeDBClusterAutomatedBackupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBClusterAutomatedBackupsPaginator(_DescribeDBClusterAutomatedBackupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBClusterAutomatedBackups.html#RDS.Paginator.DescribeDBClusterAutomatedBackups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbclusterautomatedbackupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBClusterAutomatedBackupsMessagePaginateTypeDef]
    ) -> PageIterator[DBClusterAutomatedBackupMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBClusterAutomatedBackups.html#RDS.Paginator.DescribeDBClusterAutomatedBackups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbclusterautomatedbackupspaginator)
        """

if TYPE_CHECKING:
    _DescribeDBClusterBacktracksPaginatorBase = Paginator[DBClusterBacktrackMessageTypeDef]
else:
    _DescribeDBClusterBacktracksPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBClusterBacktracksPaginator(_DescribeDBClusterBacktracksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBClusterBacktracks.html#RDS.Paginator.DescribeDBClusterBacktracks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbclusterbacktrackspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBClusterBacktracksMessagePaginateTypeDef]
    ) -> PageIterator[DBClusterBacktrackMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBClusterBacktracks.html#RDS.Paginator.DescribeDBClusterBacktracks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbclusterbacktrackspaginator)
        """

if TYPE_CHECKING:
    _DescribeDBClusterEndpointsPaginatorBase = Paginator[DBClusterEndpointMessageTypeDef]
else:
    _DescribeDBClusterEndpointsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBClusterEndpointsPaginator(_DescribeDBClusterEndpointsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBClusterEndpoints.html#RDS.Paginator.DescribeDBClusterEndpoints)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbclusterendpointspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBClusterEndpointsMessagePaginateTypeDef]
    ) -> PageIterator[DBClusterEndpointMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBClusterEndpoints.html#RDS.Paginator.DescribeDBClusterEndpoints.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbclusterendpointspaginator)
        """

if TYPE_CHECKING:
    _DescribeDBClusterParameterGroupsPaginatorBase = Paginator[
        DBClusterParameterGroupsMessageTypeDef
    ]
else:
    _DescribeDBClusterParameterGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBClusterParameterGroupsPaginator(_DescribeDBClusterParameterGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBClusterParameterGroups.html#RDS.Paginator.DescribeDBClusterParameterGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbclusterparametergroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBClusterParameterGroupsMessagePaginateTypeDef]
    ) -> PageIterator[DBClusterParameterGroupsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBClusterParameterGroups.html#RDS.Paginator.DescribeDBClusterParameterGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbclusterparametergroupspaginator)
        """

if TYPE_CHECKING:
    _DescribeDBClusterParametersPaginatorBase = Paginator[DBClusterParameterGroupDetailsTypeDef]
else:
    _DescribeDBClusterParametersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBClusterParametersPaginator(_DescribeDBClusterParametersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBClusterParameters.html#RDS.Paginator.DescribeDBClusterParameters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbclusterparameterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBClusterParametersMessagePaginateTypeDef]
    ) -> PageIterator[DBClusterParameterGroupDetailsTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBClusterParameters.html#RDS.Paginator.DescribeDBClusterParameters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbclusterparameterspaginator)
        """

if TYPE_CHECKING:
    _DescribeDBClusterSnapshotsPaginatorBase = Paginator[DBClusterSnapshotMessageTypeDef]
else:
    _DescribeDBClusterSnapshotsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBClusterSnapshotsPaginator(_DescribeDBClusterSnapshotsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBClusterSnapshots.html#RDS.Paginator.DescribeDBClusterSnapshots)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbclustersnapshotspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBClusterSnapshotsMessagePaginateTypeDef]
    ) -> PageIterator[DBClusterSnapshotMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBClusterSnapshots.html#RDS.Paginator.DescribeDBClusterSnapshots.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbclustersnapshotspaginator)
        """

if TYPE_CHECKING:
    _DescribeDBClustersPaginatorBase = Paginator[DBClusterMessageTypeDef]
else:
    _DescribeDBClustersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBClustersPaginator(_DescribeDBClustersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBClusters.html#RDS.Paginator.DescribeDBClusters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbclusterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBClustersMessagePaginateTypeDef]
    ) -> PageIterator[DBClusterMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBClusters.html#RDS.Paginator.DescribeDBClusters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbclusterspaginator)
        """

if TYPE_CHECKING:
    _DescribeDBEngineVersionsPaginatorBase = Paginator[DBEngineVersionMessageTypeDef]
else:
    _DescribeDBEngineVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBEngineVersionsPaginator(_DescribeDBEngineVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBEngineVersions.html#RDS.Paginator.DescribeDBEngineVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbengineversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBEngineVersionsMessagePaginateTypeDef]
    ) -> PageIterator[DBEngineVersionMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBEngineVersions.html#RDS.Paginator.DescribeDBEngineVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbengineversionspaginator)
        """

if TYPE_CHECKING:
    _DescribeDBInstanceAutomatedBackupsPaginatorBase = Paginator[
        DBInstanceAutomatedBackupMessageTypeDef
    ]
else:
    _DescribeDBInstanceAutomatedBackupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBInstanceAutomatedBackupsPaginator(_DescribeDBInstanceAutomatedBackupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBInstanceAutomatedBackups.html#RDS.Paginator.DescribeDBInstanceAutomatedBackups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbinstanceautomatedbackupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBInstanceAutomatedBackupsMessagePaginateTypeDef]
    ) -> PageIterator[DBInstanceAutomatedBackupMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBInstanceAutomatedBackups.html#RDS.Paginator.DescribeDBInstanceAutomatedBackups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbinstanceautomatedbackupspaginator)
        """

if TYPE_CHECKING:
    _DescribeDBInstancesPaginatorBase = Paginator[DBInstanceMessageTypeDef]
else:
    _DescribeDBInstancesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBInstancesPaginator(_DescribeDBInstancesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBInstances.html#RDS.Paginator.DescribeDBInstances)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbinstancespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBInstancesMessagePaginateTypeDef]
    ) -> PageIterator[DBInstanceMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBInstances.html#RDS.Paginator.DescribeDBInstances.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbinstancespaginator)
        """

if TYPE_CHECKING:
    _DescribeDBLogFilesPaginatorBase = Paginator[DescribeDBLogFilesResponseTypeDef]
else:
    _DescribeDBLogFilesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBLogFilesPaginator(_DescribeDBLogFilesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBLogFiles.html#RDS.Paginator.DescribeDBLogFiles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedblogfilespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBLogFilesMessagePaginateTypeDef]
    ) -> PageIterator[DescribeDBLogFilesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBLogFiles.html#RDS.Paginator.DescribeDBLogFiles.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedblogfilespaginator)
        """

if TYPE_CHECKING:
    _DescribeDBParameterGroupsPaginatorBase = Paginator[DBParameterGroupsMessageTypeDef]
else:
    _DescribeDBParameterGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBParameterGroupsPaginator(_DescribeDBParameterGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBParameterGroups.html#RDS.Paginator.DescribeDBParameterGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbparametergroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBParameterGroupsMessagePaginateTypeDef]
    ) -> PageIterator[DBParameterGroupsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBParameterGroups.html#RDS.Paginator.DescribeDBParameterGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbparametergroupspaginator)
        """

if TYPE_CHECKING:
    _DescribeDBParametersPaginatorBase = Paginator[DBParameterGroupDetailsTypeDef]
else:
    _DescribeDBParametersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBParametersPaginator(_DescribeDBParametersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBParameters.html#RDS.Paginator.DescribeDBParameters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbparameterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBParametersMessagePaginateTypeDef]
    ) -> PageIterator[DBParameterGroupDetailsTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBParameters.html#RDS.Paginator.DescribeDBParameters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbparameterspaginator)
        """

if TYPE_CHECKING:
    _DescribeDBProxiesPaginatorBase = Paginator[DescribeDBProxiesResponseTypeDef]
else:
    _DescribeDBProxiesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBProxiesPaginator(_DescribeDBProxiesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBProxies.html#RDS.Paginator.DescribeDBProxies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbproxiespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBProxiesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeDBProxiesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBProxies.html#RDS.Paginator.DescribeDBProxies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbproxiespaginator)
        """

if TYPE_CHECKING:
    _DescribeDBProxyEndpointsPaginatorBase = Paginator[DescribeDBProxyEndpointsResponseTypeDef]
else:
    _DescribeDBProxyEndpointsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBProxyEndpointsPaginator(_DescribeDBProxyEndpointsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBProxyEndpoints.html#RDS.Paginator.DescribeDBProxyEndpoints)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbproxyendpointspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBProxyEndpointsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeDBProxyEndpointsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBProxyEndpoints.html#RDS.Paginator.DescribeDBProxyEndpoints.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbproxyendpointspaginator)
        """

if TYPE_CHECKING:
    _DescribeDBProxyTargetGroupsPaginatorBase = Paginator[
        DescribeDBProxyTargetGroupsResponseTypeDef
    ]
else:
    _DescribeDBProxyTargetGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBProxyTargetGroupsPaginator(_DescribeDBProxyTargetGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBProxyTargetGroups.html#RDS.Paginator.DescribeDBProxyTargetGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbproxytargetgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBProxyTargetGroupsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeDBProxyTargetGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBProxyTargetGroups.html#RDS.Paginator.DescribeDBProxyTargetGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbproxytargetgroupspaginator)
        """

if TYPE_CHECKING:
    _DescribeDBProxyTargetsPaginatorBase = Paginator[DescribeDBProxyTargetsResponseTypeDef]
else:
    _DescribeDBProxyTargetsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBProxyTargetsPaginator(_DescribeDBProxyTargetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBProxyTargets.html#RDS.Paginator.DescribeDBProxyTargets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbproxytargetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBProxyTargetsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeDBProxyTargetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBProxyTargets.html#RDS.Paginator.DescribeDBProxyTargets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbproxytargetspaginator)
        """

if TYPE_CHECKING:
    _DescribeDBRecommendationsPaginatorBase = Paginator[DBRecommendationsMessageTypeDef]
else:
    _DescribeDBRecommendationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBRecommendationsPaginator(_DescribeDBRecommendationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBRecommendations.html#RDS.Paginator.DescribeDBRecommendations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbrecommendationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBRecommendationsMessagePaginateTypeDef]
    ) -> PageIterator[DBRecommendationsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBRecommendations.html#RDS.Paginator.DescribeDBRecommendations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbrecommendationspaginator)
        """

if TYPE_CHECKING:
    _DescribeDBSecurityGroupsPaginatorBase = Paginator[DBSecurityGroupMessageTypeDef]
else:
    _DescribeDBSecurityGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBSecurityGroupsPaginator(_DescribeDBSecurityGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBSecurityGroups.html#RDS.Paginator.DescribeDBSecurityGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbsecuritygroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBSecurityGroupsMessagePaginateTypeDef]
    ) -> PageIterator[DBSecurityGroupMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBSecurityGroups.html#RDS.Paginator.DescribeDBSecurityGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbsecuritygroupspaginator)
        """

if TYPE_CHECKING:
    _DescribeDBSnapshotTenantDatabasesPaginatorBase = Paginator[
        DBSnapshotTenantDatabasesMessageTypeDef
    ]
else:
    _DescribeDBSnapshotTenantDatabasesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBSnapshotTenantDatabasesPaginator(_DescribeDBSnapshotTenantDatabasesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBSnapshotTenantDatabases.html#RDS.Paginator.DescribeDBSnapshotTenantDatabases)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbsnapshottenantdatabasespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBSnapshotTenantDatabasesMessagePaginateTypeDef]
    ) -> PageIterator[DBSnapshotTenantDatabasesMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBSnapshotTenantDatabases.html#RDS.Paginator.DescribeDBSnapshotTenantDatabases.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbsnapshottenantdatabasespaginator)
        """

if TYPE_CHECKING:
    _DescribeDBSnapshotsPaginatorBase = Paginator[DBSnapshotMessageTypeDef]
else:
    _DescribeDBSnapshotsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBSnapshotsPaginator(_DescribeDBSnapshotsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBSnapshots.html#RDS.Paginator.DescribeDBSnapshots)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbsnapshotspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBSnapshotsMessagePaginateTypeDef]
    ) -> PageIterator[DBSnapshotMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBSnapshots.html#RDS.Paginator.DescribeDBSnapshots.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbsnapshotspaginator)
        """

if TYPE_CHECKING:
    _DescribeDBSubnetGroupsPaginatorBase = Paginator[DBSubnetGroupMessageTypeDef]
else:
    _DescribeDBSubnetGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDBSubnetGroupsPaginator(_DescribeDBSubnetGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBSubnetGroups.html#RDS.Paginator.DescribeDBSubnetGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbsubnetgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDBSubnetGroupsMessagePaginateTypeDef]
    ) -> PageIterator[DBSubnetGroupMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeDBSubnetGroups.html#RDS.Paginator.DescribeDBSubnetGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describedbsubnetgroupspaginator)
        """

if TYPE_CHECKING:
    _DescribeEngineDefaultClusterParametersPaginatorBase = Paginator[
        DescribeEngineDefaultClusterParametersResultTypeDef
    ]
else:
    _DescribeEngineDefaultClusterParametersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeEngineDefaultClusterParametersPaginator(
    _DescribeEngineDefaultClusterParametersPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeEngineDefaultClusterParameters.html#RDS.Paginator.DescribeEngineDefaultClusterParameters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describeenginedefaultclusterparameterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEngineDefaultClusterParametersMessagePaginateTypeDef]
    ) -> PageIterator[DescribeEngineDefaultClusterParametersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeEngineDefaultClusterParameters.html#RDS.Paginator.DescribeEngineDefaultClusterParameters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describeenginedefaultclusterparameterspaginator)
        """

if TYPE_CHECKING:
    _DescribeEngineDefaultParametersPaginatorBase = Paginator[
        DescribeEngineDefaultParametersResultTypeDef
    ]
else:
    _DescribeEngineDefaultParametersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeEngineDefaultParametersPaginator(_DescribeEngineDefaultParametersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeEngineDefaultParameters.html#RDS.Paginator.DescribeEngineDefaultParameters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describeenginedefaultparameterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEngineDefaultParametersMessagePaginateTypeDef]
    ) -> PageIterator[DescribeEngineDefaultParametersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeEngineDefaultParameters.html#RDS.Paginator.DescribeEngineDefaultParameters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describeenginedefaultparameterspaginator)
        """

if TYPE_CHECKING:
    _DescribeEventSubscriptionsPaginatorBase = Paginator[EventSubscriptionsMessageTypeDef]
else:
    _DescribeEventSubscriptionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeEventSubscriptionsPaginator(_DescribeEventSubscriptionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeEventSubscriptions.html#RDS.Paginator.DescribeEventSubscriptions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describeeventsubscriptionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEventSubscriptionsMessagePaginateTypeDef]
    ) -> PageIterator[EventSubscriptionsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeEventSubscriptions.html#RDS.Paginator.DescribeEventSubscriptions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describeeventsubscriptionspaginator)
        """

if TYPE_CHECKING:
    _DescribeEventsPaginatorBase = Paginator[EventsMessageTypeDef]
else:
    _DescribeEventsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeEventsPaginator(_DescribeEventsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeEvents.html#RDS.Paginator.DescribeEvents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describeeventspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEventsMessagePaginateTypeDef]
    ) -> PageIterator[EventsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeEvents.html#RDS.Paginator.DescribeEvents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describeeventspaginator)
        """

if TYPE_CHECKING:
    _DescribeExportTasksPaginatorBase = Paginator[ExportTasksMessageTypeDef]
else:
    _DescribeExportTasksPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeExportTasksPaginator(_DescribeExportTasksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeExportTasks.html#RDS.Paginator.DescribeExportTasks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describeexporttaskspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeExportTasksMessagePaginateTypeDef]
    ) -> PageIterator[ExportTasksMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeExportTasks.html#RDS.Paginator.DescribeExportTasks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describeexporttaskspaginator)
        """

if TYPE_CHECKING:
    _DescribeGlobalClustersPaginatorBase = Paginator[GlobalClustersMessageTypeDef]
else:
    _DescribeGlobalClustersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeGlobalClustersPaginator(_DescribeGlobalClustersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeGlobalClusters.html#RDS.Paginator.DescribeGlobalClusters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describeglobalclusterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeGlobalClustersMessagePaginateTypeDef]
    ) -> PageIterator[GlobalClustersMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeGlobalClusters.html#RDS.Paginator.DescribeGlobalClusters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describeglobalclusterspaginator)
        """

if TYPE_CHECKING:
    _DescribeIntegrationsPaginatorBase = Paginator[DescribeIntegrationsResponseTypeDef]
else:
    _DescribeIntegrationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeIntegrationsPaginator(_DescribeIntegrationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeIntegrations.html#RDS.Paginator.DescribeIntegrations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describeintegrationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeIntegrationsMessagePaginateTypeDef]
    ) -> PageIterator[DescribeIntegrationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeIntegrations.html#RDS.Paginator.DescribeIntegrations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describeintegrationspaginator)
        """

if TYPE_CHECKING:
    _DescribeOptionGroupOptionsPaginatorBase = Paginator[OptionGroupOptionsMessageTypeDef]
else:
    _DescribeOptionGroupOptionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeOptionGroupOptionsPaginator(_DescribeOptionGroupOptionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeOptionGroupOptions.html#RDS.Paginator.DescribeOptionGroupOptions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describeoptiongroupoptionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeOptionGroupOptionsMessagePaginateTypeDef]
    ) -> PageIterator[OptionGroupOptionsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeOptionGroupOptions.html#RDS.Paginator.DescribeOptionGroupOptions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describeoptiongroupoptionspaginator)
        """

if TYPE_CHECKING:
    _DescribeOptionGroupsPaginatorBase = Paginator[OptionGroupsTypeDef]
else:
    _DescribeOptionGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeOptionGroupsPaginator(_DescribeOptionGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeOptionGroups.html#RDS.Paginator.DescribeOptionGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describeoptiongroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeOptionGroupsMessagePaginateTypeDef]
    ) -> PageIterator[OptionGroupsTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeOptionGroups.html#RDS.Paginator.DescribeOptionGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describeoptiongroupspaginator)
        """

if TYPE_CHECKING:
    _DescribeOrderableDBInstanceOptionsPaginatorBase = Paginator[
        OrderableDBInstanceOptionsMessageTypeDef
    ]
else:
    _DescribeOrderableDBInstanceOptionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeOrderableDBInstanceOptionsPaginator(_DescribeOrderableDBInstanceOptionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeOrderableDBInstanceOptions.html#RDS.Paginator.DescribeOrderableDBInstanceOptions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describeorderabledbinstanceoptionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeOrderableDBInstanceOptionsMessagePaginateTypeDef]
    ) -> PageIterator[OrderableDBInstanceOptionsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeOrderableDBInstanceOptions.html#RDS.Paginator.DescribeOrderableDBInstanceOptions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describeorderabledbinstanceoptionspaginator)
        """

if TYPE_CHECKING:
    _DescribePendingMaintenanceActionsPaginatorBase = Paginator[
        PendingMaintenanceActionsMessageTypeDef
    ]
else:
    _DescribePendingMaintenanceActionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribePendingMaintenanceActionsPaginator(_DescribePendingMaintenanceActionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribePendingMaintenanceActions.html#RDS.Paginator.DescribePendingMaintenanceActions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describependingmaintenanceactionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribePendingMaintenanceActionsMessagePaginateTypeDef]
    ) -> PageIterator[PendingMaintenanceActionsMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribePendingMaintenanceActions.html#RDS.Paginator.DescribePendingMaintenanceActions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describependingmaintenanceactionspaginator)
        """

if TYPE_CHECKING:
    _DescribeReservedDBInstancesOfferingsPaginatorBase = Paginator[
        ReservedDBInstancesOfferingMessageTypeDef
    ]
else:
    _DescribeReservedDBInstancesOfferingsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeReservedDBInstancesOfferingsPaginator(
    _DescribeReservedDBInstancesOfferingsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeReservedDBInstancesOfferings.html#RDS.Paginator.DescribeReservedDBInstancesOfferings)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describereserveddbinstancesofferingspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeReservedDBInstancesOfferingsMessagePaginateTypeDef]
    ) -> PageIterator[ReservedDBInstancesOfferingMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeReservedDBInstancesOfferings.html#RDS.Paginator.DescribeReservedDBInstancesOfferings.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describereserveddbinstancesofferingspaginator)
        """

if TYPE_CHECKING:
    _DescribeReservedDBInstancesPaginatorBase = Paginator[ReservedDBInstanceMessageTypeDef]
else:
    _DescribeReservedDBInstancesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeReservedDBInstancesPaginator(_DescribeReservedDBInstancesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeReservedDBInstances.html#RDS.Paginator.DescribeReservedDBInstances)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describereserveddbinstancespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeReservedDBInstancesMessagePaginateTypeDef]
    ) -> PageIterator[ReservedDBInstanceMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeReservedDBInstances.html#RDS.Paginator.DescribeReservedDBInstances.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describereserveddbinstancespaginator)
        """

if TYPE_CHECKING:
    _DescribeSourceRegionsPaginatorBase = Paginator[SourceRegionMessageTypeDef]
else:
    _DescribeSourceRegionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeSourceRegionsPaginator(_DescribeSourceRegionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeSourceRegions.html#RDS.Paginator.DescribeSourceRegions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describesourceregionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeSourceRegionsMessagePaginateTypeDef]
    ) -> PageIterator[SourceRegionMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeSourceRegions.html#RDS.Paginator.DescribeSourceRegions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describesourceregionspaginator)
        """

if TYPE_CHECKING:
    _DescribeTenantDatabasesPaginatorBase = Paginator[TenantDatabasesMessageTypeDef]
else:
    _DescribeTenantDatabasesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeTenantDatabasesPaginator(_DescribeTenantDatabasesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeTenantDatabases.html#RDS.Paginator.DescribeTenantDatabases)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describetenantdatabasespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTenantDatabasesMessagePaginateTypeDef]
    ) -> PageIterator[TenantDatabasesMessageTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DescribeTenantDatabases.html#RDS.Paginator.DescribeTenantDatabases.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#describetenantdatabasespaginator)
        """

if TYPE_CHECKING:
    _DownloadDBLogFilePortionPaginatorBase = Paginator[DownloadDBLogFilePortionDetailsTypeDef]
else:
    _DownloadDBLogFilePortionPaginatorBase = Paginator  # type: ignore[assignment]

class DownloadDBLogFilePortionPaginator(_DownloadDBLogFilePortionPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DownloadDBLogFilePortion.html#RDS.Paginator.DownloadDBLogFilePortion)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#downloaddblogfileportionpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DownloadDBLogFilePortionMessagePaginateTypeDef]
    ) -> PageIterator[DownloadDBLogFilePortionDetailsTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/paginator/DownloadDBLogFilePortion.html#RDS.Paginator.DownloadDBLogFilePortion.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/paginators/#downloaddblogfileportionpaginator)
        """
