"""
Type annotations for rds service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_rds.client import RDSClient

    session = Session()
    client: RDSClient = session.client("rds")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
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
    DescribeDBSnapshotsPaginator,
    DescribeDBSnapshotTenantDatabasesPaginator,
    DescribeDBSubnetGroupsPaginator,
    DescribeEngineDefaultClusterParametersPaginator,
    DescribeEngineDefaultParametersPaginator,
    DescribeEventsPaginator,
    DescribeEventSubscriptionsPaginator,
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
from .type_defs import (
    AccountAttributesMessageTypeDef,
    AddRoleToDBClusterMessageTypeDef,
    AddRoleToDBInstanceMessageTypeDef,
    AddSourceIdentifierToSubscriptionMessageTypeDef,
    AddSourceIdentifierToSubscriptionResultTypeDef,
    AddTagsToResourceMessageTypeDef,
    ApplyPendingMaintenanceActionMessageTypeDef,
    ApplyPendingMaintenanceActionResultTypeDef,
    AuthorizeDBSecurityGroupIngressMessageTypeDef,
    AuthorizeDBSecurityGroupIngressResultTypeDef,
    BacktrackDBClusterMessageTypeDef,
    CancelExportTaskMessageTypeDef,
    CertificateMessageTypeDef,
    CopyDBClusterParameterGroupMessageTypeDef,
    CopyDBClusterParameterGroupResultTypeDef,
    CopyDBClusterSnapshotMessageTypeDef,
    CopyDBClusterSnapshotResultTypeDef,
    CopyDBParameterGroupMessageTypeDef,
    CopyDBParameterGroupResultTypeDef,
    CopyDBSnapshotMessageTypeDef,
    CopyDBSnapshotResultTypeDef,
    CopyOptionGroupMessageTypeDef,
    CopyOptionGroupResultTypeDef,
    CreateBlueGreenDeploymentRequestTypeDef,
    CreateBlueGreenDeploymentResponseTypeDef,
    CreateCustomDBEngineVersionMessageTypeDef,
    CreateDBClusterEndpointMessageTypeDef,
    CreateDBClusterMessageTypeDef,
    CreateDBClusterParameterGroupMessageTypeDef,
    CreateDBClusterParameterGroupResultTypeDef,
    CreateDBClusterResultTypeDef,
    CreateDBClusterSnapshotMessageTypeDef,
    CreateDBClusterSnapshotResultTypeDef,
    CreateDBInstanceMessageTypeDef,
    CreateDBInstanceReadReplicaMessageTypeDef,
    CreateDBInstanceReadReplicaResultTypeDef,
    CreateDBInstanceResultTypeDef,
    CreateDBParameterGroupMessageTypeDef,
    CreateDBParameterGroupResultTypeDef,
    CreateDBProxyEndpointRequestTypeDef,
    CreateDBProxyEndpointResponseTypeDef,
    CreateDBProxyRequestTypeDef,
    CreateDBProxyResponseTypeDef,
    CreateDBSecurityGroupMessageTypeDef,
    CreateDBSecurityGroupResultTypeDef,
    CreateDBShardGroupMessageTypeDef,
    CreateDBSnapshotMessageTypeDef,
    CreateDBSnapshotResultTypeDef,
    CreateDBSubnetGroupMessageTypeDef,
    CreateDBSubnetGroupResultTypeDef,
    CreateEventSubscriptionMessageTypeDef,
    CreateEventSubscriptionResultTypeDef,
    CreateGlobalClusterMessageTypeDef,
    CreateGlobalClusterResultTypeDef,
    CreateIntegrationMessageTypeDef,
    CreateOptionGroupMessageTypeDef,
    CreateOptionGroupResultTypeDef,
    CreateTenantDatabaseMessageTypeDef,
    CreateTenantDatabaseResultTypeDef,
    DBClusterAutomatedBackupMessageTypeDef,
    DBClusterBacktrackMessageTypeDef,
    DBClusterBacktrackResponseTypeDef,
    DBClusterCapacityInfoTypeDef,
    DBClusterEndpointMessageTypeDef,
    DBClusterEndpointResponseTypeDef,
    DBClusterMessageTypeDef,
    DBClusterParameterGroupDetailsTypeDef,
    DBClusterParameterGroupNameMessageTypeDef,
    DBClusterParameterGroupsMessageTypeDef,
    DBClusterSnapshotMessageTypeDef,
    DBEngineVersionMessageTypeDef,
    DBEngineVersionResponseTypeDef,
    DBInstanceAutomatedBackupMessageTypeDef,
    DBInstanceMessageTypeDef,
    DBParameterGroupDetailsTypeDef,
    DBParameterGroupNameMessageTypeDef,
    DBParameterGroupsMessageTypeDef,
    DBRecommendationMessageTypeDef,
    DBRecommendationsMessageTypeDef,
    DBSecurityGroupMessageTypeDef,
    DBShardGroupResponseTypeDef,
    DBSnapshotMessageTypeDef,
    DBSnapshotTenantDatabasesMessageTypeDef,
    DBSubnetGroupMessageTypeDef,
    DeleteBlueGreenDeploymentRequestTypeDef,
    DeleteBlueGreenDeploymentResponseTypeDef,
    DeleteCustomDBEngineVersionMessageTypeDef,
    DeleteDBClusterAutomatedBackupMessageTypeDef,
    DeleteDBClusterAutomatedBackupResultTypeDef,
    DeleteDBClusterEndpointMessageTypeDef,
    DeleteDBClusterMessageTypeDef,
    DeleteDBClusterParameterGroupMessageTypeDef,
    DeleteDBClusterResultTypeDef,
    DeleteDBClusterSnapshotMessageTypeDef,
    DeleteDBClusterSnapshotResultTypeDef,
    DeleteDBInstanceAutomatedBackupMessageTypeDef,
    DeleteDBInstanceAutomatedBackupResultTypeDef,
    DeleteDBInstanceMessageTypeDef,
    DeleteDBInstanceResultTypeDef,
    DeleteDBParameterGroupMessageTypeDef,
    DeleteDBProxyEndpointRequestTypeDef,
    DeleteDBProxyEndpointResponseTypeDef,
    DeleteDBProxyRequestTypeDef,
    DeleteDBProxyResponseTypeDef,
    DeleteDBSecurityGroupMessageTypeDef,
    DeleteDBShardGroupMessageTypeDef,
    DeleteDBSnapshotMessageTypeDef,
    DeleteDBSnapshotResultTypeDef,
    DeleteDBSubnetGroupMessageTypeDef,
    DeleteEventSubscriptionMessageTypeDef,
    DeleteEventSubscriptionResultTypeDef,
    DeleteGlobalClusterMessageTypeDef,
    DeleteGlobalClusterResultTypeDef,
    DeleteIntegrationMessageTypeDef,
    DeleteOptionGroupMessageTypeDef,
    DeleteTenantDatabaseMessageTypeDef,
    DeleteTenantDatabaseResultTypeDef,
    DeregisterDBProxyTargetsRequestTypeDef,
    DescribeBlueGreenDeploymentsRequestTypeDef,
    DescribeBlueGreenDeploymentsResponseTypeDef,
    DescribeCertificatesMessageTypeDef,
    DescribeDBClusterAutomatedBackupsMessageTypeDef,
    DescribeDBClusterBacktracksMessageTypeDef,
    DescribeDBClusterEndpointsMessageTypeDef,
    DescribeDBClusterParameterGroupsMessageTypeDef,
    DescribeDBClusterParametersMessageTypeDef,
    DescribeDBClustersMessageTypeDef,
    DescribeDBClusterSnapshotAttributesMessageTypeDef,
    DescribeDBClusterSnapshotAttributesResultTypeDef,
    DescribeDBClusterSnapshotsMessageTypeDef,
    DescribeDBEngineVersionsMessageTypeDef,
    DescribeDBInstanceAutomatedBackupsMessageTypeDef,
    DescribeDBInstancesMessageTypeDef,
    DescribeDBLogFilesMessageTypeDef,
    DescribeDBLogFilesResponseTypeDef,
    DescribeDBParameterGroupsMessageTypeDef,
    DescribeDBParametersMessageTypeDef,
    DescribeDBProxiesRequestTypeDef,
    DescribeDBProxiesResponseTypeDef,
    DescribeDBProxyEndpointsRequestTypeDef,
    DescribeDBProxyEndpointsResponseTypeDef,
    DescribeDBProxyTargetGroupsRequestTypeDef,
    DescribeDBProxyTargetGroupsResponseTypeDef,
    DescribeDBProxyTargetsRequestTypeDef,
    DescribeDBProxyTargetsResponseTypeDef,
    DescribeDBRecommendationsMessageTypeDef,
    DescribeDBSecurityGroupsMessageTypeDef,
    DescribeDBShardGroupsMessageTypeDef,
    DescribeDBShardGroupsResponseTypeDef,
    DescribeDBSnapshotAttributesMessageTypeDef,
    DescribeDBSnapshotAttributesResultTypeDef,
    DescribeDBSnapshotsMessageTypeDef,
    DescribeDBSnapshotTenantDatabasesMessageTypeDef,
    DescribeDBSubnetGroupsMessageTypeDef,
    DescribeEngineDefaultClusterParametersMessageTypeDef,
    DescribeEngineDefaultClusterParametersResultTypeDef,
    DescribeEngineDefaultParametersMessageTypeDef,
    DescribeEngineDefaultParametersResultTypeDef,
    DescribeEventCategoriesMessageTypeDef,
    DescribeEventsMessageTypeDef,
    DescribeEventSubscriptionsMessageTypeDef,
    DescribeExportTasksMessageTypeDef,
    DescribeGlobalClustersMessageTypeDef,
    DescribeIntegrationsMessageTypeDef,
    DescribeIntegrationsResponseTypeDef,
    DescribeOptionGroupOptionsMessageTypeDef,
    DescribeOptionGroupsMessageTypeDef,
    DescribeOrderableDBInstanceOptionsMessageTypeDef,
    DescribePendingMaintenanceActionsMessageTypeDef,
    DescribeReservedDBInstancesMessageTypeDef,
    DescribeReservedDBInstancesOfferingsMessageTypeDef,
    DescribeSourceRegionsMessageTypeDef,
    DescribeTenantDatabasesMessageTypeDef,
    DescribeValidDBInstanceModificationsMessageTypeDef,
    DescribeValidDBInstanceModificationsResultTypeDef,
    DisableHttpEndpointRequestTypeDef,
    DisableHttpEndpointResponseTypeDef,
    DownloadDBLogFilePortionDetailsTypeDef,
    DownloadDBLogFilePortionMessageTypeDef,
    EmptyResponseMetadataTypeDef,
    EnableHttpEndpointRequestTypeDef,
    EnableHttpEndpointResponseTypeDef,
    EventCategoriesMessageTypeDef,
    EventsMessageTypeDef,
    EventSubscriptionsMessageTypeDef,
    ExportTaskResponseTypeDef,
    ExportTasksMessageTypeDef,
    FailoverDBClusterMessageTypeDef,
    FailoverDBClusterResultTypeDef,
    FailoverGlobalClusterMessageTypeDef,
    FailoverGlobalClusterResultTypeDef,
    GlobalClustersMessageTypeDef,
    IntegrationResponseTypeDef,
    ListTagsForResourceMessageTypeDef,
    ModifyActivityStreamRequestTypeDef,
    ModifyActivityStreamResponseTypeDef,
    ModifyCertificatesMessageTypeDef,
    ModifyCertificatesResultTypeDef,
    ModifyCurrentDBClusterCapacityMessageTypeDef,
    ModifyCustomDBEngineVersionMessageTypeDef,
    ModifyDBClusterEndpointMessageTypeDef,
    ModifyDBClusterMessageTypeDef,
    ModifyDBClusterParameterGroupMessageTypeDef,
    ModifyDBClusterResultTypeDef,
    ModifyDBClusterSnapshotAttributeMessageTypeDef,
    ModifyDBClusterSnapshotAttributeResultTypeDef,
    ModifyDBInstanceMessageTypeDef,
    ModifyDBInstanceResultTypeDef,
    ModifyDBParameterGroupMessageTypeDef,
    ModifyDBProxyEndpointRequestTypeDef,
    ModifyDBProxyEndpointResponseTypeDef,
    ModifyDBProxyRequestTypeDef,
    ModifyDBProxyResponseTypeDef,
    ModifyDBProxyTargetGroupRequestTypeDef,
    ModifyDBProxyTargetGroupResponseTypeDef,
    ModifyDBRecommendationMessageTypeDef,
    ModifyDBShardGroupMessageTypeDef,
    ModifyDBSnapshotAttributeMessageTypeDef,
    ModifyDBSnapshotAttributeResultTypeDef,
    ModifyDBSnapshotMessageTypeDef,
    ModifyDBSnapshotResultTypeDef,
    ModifyDBSubnetGroupMessageTypeDef,
    ModifyDBSubnetGroupResultTypeDef,
    ModifyEventSubscriptionMessageTypeDef,
    ModifyEventSubscriptionResultTypeDef,
    ModifyGlobalClusterMessageTypeDef,
    ModifyGlobalClusterResultTypeDef,
    ModifyIntegrationMessageTypeDef,
    ModifyOptionGroupMessageTypeDef,
    ModifyOptionGroupResultTypeDef,
    ModifyTenantDatabaseMessageTypeDef,
    ModifyTenantDatabaseResultTypeDef,
    OptionGroupOptionsMessageTypeDef,
    OptionGroupsTypeDef,
    OrderableDBInstanceOptionsMessageTypeDef,
    PendingMaintenanceActionsMessageTypeDef,
    PromoteReadReplicaDBClusterMessageTypeDef,
    PromoteReadReplicaDBClusterResultTypeDef,
    PromoteReadReplicaMessageTypeDef,
    PromoteReadReplicaResultTypeDef,
    PurchaseReservedDBInstancesOfferingMessageTypeDef,
    PurchaseReservedDBInstancesOfferingResultTypeDef,
    RebootDBClusterMessageTypeDef,
    RebootDBClusterResultTypeDef,
    RebootDBInstanceMessageTypeDef,
    RebootDBInstanceResultTypeDef,
    RebootDBShardGroupMessageTypeDef,
    RegisterDBProxyTargetsRequestTypeDef,
    RegisterDBProxyTargetsResponseTypeDef,
    RemoveFromGlobalClusterMessageTypeDef,
    RemoveFromGlobalClusterResultTypeDef,
    RemoveRoleFromDBClusterMessageTypeDef,
    RemoveRoleFromDBInstanceMessageTypeDef,
    RemoveSourceIdentifierFromSubscriptionMessageTypeDef,
    RemoveSourceIdentifierFromSubscriptionResultTypeDef,
    RemoveTagsFromResourceMessageTypeDef,
    ReservedDBInstanceMessageTypeDef,
    ReservedDBInstancesOfferingMessageTypeDef,
    ResetDBClusterParameterGroupMessageTypeDef,
    ResetDBParameterGroupMessageTypeDef,
    RestoreDBClusterFromS3MessageTypeDef,
    RestoreDBClusterFromS3ResultTypeDef,
    RestoreDBClusterFromSnapshotMessageTypeDef,
    RestoreDBClusterFromSnapshotResultTypeDef,
    RestoreDBClusterToPointInTimeMessageTypeDef,
    RestoreDBClusterToPointInTimeResultTypeDef,
    RestoreDBInstanceFromDBSnapshotMessageTypeDef,
    RestoreDBInstanceFromDBSnapshotResultTypeDef,
    RestoreDBInstanceFromS3MessageTypeDef,
    RestoreDBInstanceFromS3ResultTypeDef,
    RestoreDBInstanceToPointInTimeMessageTypeDef,
    RestoreDBInstanceToPointInTimeResultTypeDef,
    RevokeDBSecurityGroupIngressMessageTypeDef,
    RevokeDBSecurityGroupIngressResultTypeDef,
    SourceRegionMessageTypeDef,
    StartActivityStreamRequestTypeDef,
    StartActivityStreamResponseTypeDef,
    StartDBClusterMessageTypeDef,
    StartDBClusterResultTypeDef,
    StartDBInstanceAutomatedBackupsReplicationMessageTypeDef,
    StartDBInstanceAutomatedBackupsReplicationResultTypeDef,
    StartDBInstanceMessageTypeDef,
    StartDBInstanceResultTypeDef,
    StartExportTaskMessageTypeDef,
    StopActivityStreamRequestTypeDef,
    StopActivityStreamResponseTypeDef,
    StopDBClusterMessageTypeDef,
    StopDBClusterResultTypeDef,
    StopDBInstanceAutomatedBackupsReplicationMessageTypeDef,
    StopDBInstanceAutomatedBackupsReplicationResultTypeDef,
    StopDBInstanceMessageTypeDef,
    StopDBInstanceResultTypeDef,
    SwitchoverBlueGreenDeploymentRequestTypeDef,
    SwitchoverBlueGreenDeploymentResponseTypeDef,
    SwitchoverGlobalClusterMessageTypeDef,
    SwitchoverGlobalClusterResultTypeDef,
    SwitchoverReadReplicaMessageTypeDef,
    SwitchoverReadReplicaResultTypeDef,
    TagListMessageTypeDef,
    TenantDatabasesMessageTypeDef,
)
from .waiter import (
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

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack


__all__ = ("RDSClient",)


class Exceptions(BaseClientExceptions):
    AuthorizationAlreadyExistsFault: Type[BotocoreClientError]
    AuthorizationNotFoundFault: Type[BotocoreClientError]
    AuthorizationQuotaExceededFault: Type[BotocoreClientError]
    BackupPolicyNotFoundFault: Type[BotocoreClientError]
    BlueGreenDeploymentAlreadyExistsFault: Type[BotocoreClientError]
    BlueGreenDeploymentNotFoundFault: Type[BotocoreClientError]
    CertificateNotFoundFault: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    CreateCustomDBEngineVersionFault: Type[BotocoreClientError]
    CustomAvailabilityZoneNotFoundFault: Type[BotocoreClientError]
    CustomDBEngineVersionAlreadyExistsFault: Type[BotocoreClientError]
    CustomDBEngineVersionNotFoundFault: Type[BotocoreClientError]
    CustomDBEngineVersionQuotaExceededFault: Type[BotocoreClientError]
    DBClusterAlreadyExistsFault: Type[BotocoreClientError]
    DBClusterAutomatedBackupNotFoundFault: Type[BotocoreClientError]
    DBClusterAutomatedBackupQuotaExceededFault: Type[BotocoreClientError]
    DBClusterBacktrackNotFoundFault: Type[BotocoreClientError]
    DBClusterEndpointAlreadyExistsFault: Type[BotocoreClientError]
    DBClusterEndpointNotFoundFault: Type[BotocoreClientError]
    DBClusterEndpointQuotaExceededFault: Type[BotocoreClientError]
    DBClusterNotFoundFault: Type[BotocoreClientError]
    DBClusterParameterGroupNotFoundFault: Type[BotocoreClientError]
    DBClusterQuotaExceededFault: Type[BotocoreClientError]
    DBClusterRoleAlreadyExistsFault: Type[BotocoreClientError]
    DBClusterRoleNotFoundFault: Type[BotocoreClientError]
    DBClusterRoleQuotaExceededFault: Type[BotocoreClientError]
    DBClusterSnapshotAlreadyExistsFault: Type[BotocoreClientError]
    DBClusterSnapshotNotFoundFault: Type[BotocoreClientError]
    DBInstanceAlreadyExistsFault: Type[BotocoreClientError]
    DBInstanceAutomatedBackupNotFoundFault: Type[BotocoreClientError]
    DBInstanceAutomatedBackupQuotaExceededFault: Type[BotocoreClientError]
    DBInstanceNotFoundFault: Type[BotocoreClientError]
    DBInstanceNotReadyFault: Type[BotocoreClientError]
    DBInstanceRoleAlreadyExistsFault: Type[BotocoreClientError]
    DBInstanceRoleNotFoundFault: Type[BotocoreClientError]
    DBInstanceRoleQuotaExceededFault: Type[BotocoreClientError]
    DBLogFileNotFoundFault: Type[BotocoreClientError]
    DBParameterGroupAlreadyExistsFault: Type[BotocoreClientError]
    DBParameterGroupNotFoundFault: Type[BotocoreClientError]
    DBParameterGroupQuotaExceededFault: Type[BotocoreClientError]
    DBProxyAlreadyExistsFault: Type[BotocoreClientError]
    DBProxyEndpointAlreadyExistsFault: Type[BotocoreClientError]
    DBProxyEndpointNotFoundFault: Type[BotocoreClientError]
    DBProxyEndpointQuotaExceededFault: Type[BotocoreClientError]
    DBProxyNotFoundFault: Type[BotocoreClientError]
    DBProxyQuotaExceededFault: Type[BotocoreClientError]
    DBProxyTargetAlreadyRegisteredFault: Type[BotocoreClientError]
    DBProxyTargetGroupNotFoundFault: Type[BotocoreClientError]
    DBProxyTargetNotFoundFault: Type[BotocoreClientError]
    DBSecurityGroupAlreadyExistsFault: Type[BotocoreClientError]
    DBSecurityGroupNotFoundFault: Type[BotocoreClientError]
    DBSecurityGroupNotSupportedFault: Type[BotocoreClientError]
    DBSecurityGroupQuotaExceededFault: Type[BotocoreClientError]
    DBShardGroupAlreadyExistsFault: Type[BotocoreClientError]
    DBShardGroupNotFoundFault: Type[BotocoreClientError]
    DBSnapshotAlreadyExistsFault: Type[BotocoreClientError]
    DBSnapshotNotFoundFault: Type[BotocoreClientError]
    DBSnapshotTenantDatabaseNotFoundFault: Type[BotocoreClientError]
    DBSubnetGroupAlreadyExistsFault: Type[BotocoreClientError]
    DBSubnetGroupDoesNotCoverEnoughAZs: Type[BotocoreClientError]
    DBSubnetGroupNotAllowedFault: Type[BotocoreClientError]
    DBSubnetGroupNotFoundFault: Type[BotocoreClientError]
    DBSubnetGroupQuotaExceededFault: Type[BotocoreClientError]
    DBSubnetQuotaExceededFault: Type[BotocoreClientError]
    DBUpgradeDependencyFailureFault: Type[BotocoreClientError]
    DomainNotFoundFault: Type[BotocoreClientError]
    Ec2ImagePropertiesNotSupportedFault: Type[BotocoreClientError]
    EventSubscriptionQuotaExceededFault: Type[BotocoreClientError]
    ExportTaskAlreadyExistsFault: Type[BotocoreClientError]
    ExportTaskNotFoundFault: Type[BotocoreClientError]
    GlobalClusterAlreadyExistsFault: Type[BotocoreClientError]
    GlobalClusterNotFoundFault: Type[BotocoreClientError]
    GlobalClusterQuotaExceededFault: Type[BotocoreClientError]
    IamRoleMissingPermissionsFault: Type[BotocoreClientError]
    IamRoleNotFoundFault: Type[BotocoreClientError]
    InstanceQuotaExceededFault: Type[BotocoreClientError]
    InsufficientAvailableIPsInSubnetFault: Type[BotocoreClientError]
    InsufficientDBClusterCapacityFault: Type[BotocoreClientError]
    InsufficientDBInstanceCapacityFault: Type[BotocoreClientError]
    InsufficientStorageClusterCapacityFault: Type[BotocoreClientError]
    IntegrationAlreadyExistsFault: Type[BotocoreClientError]
    IntegrationConflictOperationFault: Type[BotocoreClientError]
    IntegrationNotFoundFault: Type[BotocoreClientError]
    IntegrationQuotaExceededFault: Type[BotocoreClientError]
    InvalidBlueGreenDeploymentStateFault: Type[BotocoreClientError]
    InvalidCustomDBEngineVersionStateFault: Type[BotocoreClientError]
    InvalidDBClusterAutomatedBackupStateFault: Type[BotocoreClientError]
    InvalidDBClusterCapacityFault: Type[BotocoreClientError]
    InvalidDBClusterEndpointStateFault: Type[BotocoreClientError]
    InvalidDBClusterSnapshotStateFault: Type[BotocoreClientError]
    InvalidDBClusterStateFault: Type[BotocoreClientError]
    InvalidDBInstanceAutomatedBackupStateFault: Type[BotocoreClientError]
    InvalidDBInstanceStateFault: Type[BotocoreClientError]
    InvalidDBParameterGroupStateFault: Type[BotocoreClientError]
    InvalidDBProxyEndpointStateFault: Type[BotocoreClientError]
    InvalidDBProxyStateFault: Type[BotocoreClientError]
    InvalidDBSecurityGroupStateFault: Type[BotocoreClientError]
    InvalidDBShardGroupStateFault: Type[BotocoreClientError]
    InvalidDBSnapshotStateFault: Type[BotocoreClientError]
    InvalidDBSubnetGroupFault: Type[BotocoreClientError]
    InvalidDBSubnetGroupStateFault: Type[BotocoreClientError]
    InvalidDBSubnetStateFault: Type[BotocoreClientError]
    InvalidEventSubscriptionStateFault: Type[BotocoreClientError]
    InvalidExportOnlyFault: Type[BotocoreClientError]
    InvalidExportSourceStateFault: Type[BotocoreClientError]
    InvalidExportTaskStateFault: Type[BotocoreClientError]
    InvalidGlobalClusterStateFault: Type[BotocoreClientError]
    InvalidIntegrationStateFault: Type[BotocoreClientError]
    InvalidOptionGroupStateFault: Type[BotocoreClientError]
    InvalidResourceStateFault: Type[BotocoreClientError]
    InvalidRestoreFault: Type[BotocoreClientError]
    InvalidS3BucketFault: Type[BotocoreClientError]
    InvalidSubnet: Type[BotocoreClientError]
    InvalidVPCNetworkStateFault: Type[BotocoreClientError]
    KMSKeyNotAccessibleFault: Type[BotocoreClientError]
    MaxDBShardGroupLimitReached: Type[BotocoreClientError]
    NetworkTypeNotSupported: Type[BotocoreClientError]
    OptionGroupAlreadyExistsFault: Type[BotocoreClientError]
    OptionGroupNotFoundFault: Type[BotocoreClientError]
    OptionGroupQuotaExceededFault: Type[BotocoreClientError]
    PointInTimeRestoreNotEnabledFault: Type[BotocoreClientError]
    ProvisionedIopsNotAvailableInAZFault: Type[BotocoreClientError]
    ReservedDBInstanceAlreadyExistsFault: Type[BotocoreClientError]
    ReservedDBInstanceNotFoundFault: Type[BotocoreClientError]
    ReservedDBInstanceQuotaExceededFault: Type[BotocoreClientError]
    ReservedDBInstancesOfferingNotFoundFault: Type[BotocoreClientError]
    ResourceNotFoundFault: Type[BotocoreClientError]
    SNSInvalidTopicFault: Type[BotocoreClientError]
    SNSNoAuthorizationFault: Type[BotocoreClientError]
    SNSTopicArnNotFoundFault: Type[BotocoreClientError]
    SharedSnapshotQuotaExceededFault: Type[BotocoreClientError]
    SnapshotQuotaExceededFault: Type[BotocoreClientError]
    SourceClusterNotSupportedFault: Type[BotocoreClientError]
    SourceDatabaseNotSupportedFault: Type[BotocoreClientError]
    SourceNotFoundFault: Type[BotocoreClientError]
    StorageQuotaExceededFault: Type[BotocoreClientError]
    StorageTypeNotAvailableFault: Type[BotocoreClientError]
    StorageTypeNotSupportedFault: Type[BotocoreClientError]
    SubnetAlreadyInUse: Type[BotocoreClientError]
    SubscriptionAlreadyExistFault: Type[BotocoreClientError]
    SubscriptionCategoryNotFoundFault: Type[BotocoreClientError]
    SubscriptionNotFoundFault: Type[BotocoreClientError]
    TenantDatabaseAlreadyExistsFault: Type[BotocoreClientError]
    TenantDatabaseNotFoundFault: Type[BotocoreClientError]
    TenantDatabaseQuotaExceededFault: Type[BotocoreClientError]
    UnsupportedDBEngineVersionFault: Type[BotocoreClientError]


class RDSClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        RDSClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#generate_presigned_url)
        """

    def add_role_to_db_cluster(
        self, **kwargs: Unpack[AddRoleToDBClusterMessageTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Associates an Identity and Access Management (IAM) role with a DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/add_role_to_db_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#add_role_to_db_cluster)
        """

    def add_role_to_db_instance(
        self, **kwargs: Unpack[AddRoleToDBInstanceMessageTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Associates an Amazon Web Services Identity and Access Management (IAM) role
        with a DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/add_role_to_db_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#add_role_to_db_instance)
        """

    def add_source_identifier_to_subscription(
        self, **kwargs: Unpack[AddSourceIdentifierToSubscriptionMessageTypeDef]
    ) -> AddSourceIdentifierToSubscriptionResultTypeDef:
        """
        Adds a source identifier to an existing RDS event notification subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/add_source_identifier_to_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#add_source_identifier_to_subscription)
        """

    def add_tags_to_resource(
        self, **kwargs: Unpack[AddTagsToResourceMessageTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds metadata tags to an Amazon RDS resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/add_tags_to_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#add_tags_to_resource)
        """

    def apply_pending_maintenance_action(
        self, **kwargs: Unpack[ApplyPendingMaintenanceActionMessageTypeDef]
    ) -> ApplyPendingMaintenanceActionResultTypeDef:
        """
        Applies a pending maintenance action to a resource (for example, to a DB
        instance).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/apply_pending_maintenance_action.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#apply_pending_maintenance_action)
        """

    def authorize_db_security_group_ingress(
        self, **kwargs: Unpack[AuthorizeDBSecurityGroupIngressMessageTypeDef]
    ) -> AuthorizeDBSecurityGroupIngressResultTypeDef:
        """
        Enables ingress to a DBSecurityGroup using one of two forms of authorization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/authorize_db_security_group_ingress.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#authorize_db_security_group_ingress)
        """

    def backtrack_db_cluster(
        self, **kwargs: Unpack[BacktrackDBClusterMessageTypeDef]
    ) -> DBClusterBacktrackResponseTypeDef:
        """
        Backtracks a DB cluster to a specific time, without creating a new DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/backtrack_db_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#backtrack_db_cluster)
        """

    def cancel_export_task(
        self, **kwargs: Unpack[CancelExportTaskMessageTypeDef]
    ) -> ExportTaskResponseTypeDef:
        """
        Cancels an export task in progress that is exporting a snapshot or cluster to
        Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/cancel_export_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#cancel_export_task)
        """

    def copy_db_cluster_parameter_group(
        self, **kwargs: Unpack[CopyDBClusterParameterGroupMessageTypeDef]
    ) -> CopyDBClusterParameterGroupResultTypeDef:
        """
        Copies the specified DB cluster parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/copy_db_cluster_parameter_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#copy_db_cluster_parameter_group)
        """

    def copy_db_cluster_snapshot(
        self, **kwargs: Unpack[CopyDBClusterSnapshotMessageTypeDef]
    ) -> CopyDBClusterSnapshotResultTypeDef:
        """
        Copies a snapshot of a DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/copy_db_cluster_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#copy_db_cluster_snapshot)
        """

    def copy_db_parameter_group(
        self, **kwargs: Unpack[CopyDBParameterGroupMessageTypeDef]
    ) -> CopyDBParameterGroupResultTypeDef:
        """
        Copies the specified DB parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/copy_db_parameter_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#copy_db_parameter_group)
        """

    def copy_db_snapshot(
        self, **kwargs: Unpack[CopyDBSnapshotMessageTypeDef]
    ) -> CopyDBSnapshotResultTypeDef:
        """
        Copies the specified DB snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/copy_db_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#copy_db_snapshot)
        """

    def copy_option_group(
        self, **kwargs: Unpack[CopyOptionGroupMessageTypeDef]
    ) -> CopyOptionGroupResultTypeDef:
        """
        Copies the specified option group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/copy_option_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#copy_option_group)
        """

    def create_blue_green_deployment(
        self, **kwargs: Unpack[CreateBlueGreenDeploymentRequestTypeDef]
    ) -> CreateBlueGreenDeploymentResponseTypeDef:
        """
        Creates a blue/green deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/create_blue_green_deployment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_blue_green_deployment)
        """

    def create_custom_db_engine_version(
        self, **kwargs: Unpack[CreateCustomDBEngineVersionMessageTypeDef]
    ) -> DBEngineVersionResponseTypeDef:
        """
        Creates a custom DB engine version (CEV).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/create_custom_db_engine_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_custom_db_engine_version)
        """

    def create_db_cluster(
        self, **kwargs: Unpack[CreateDBClusterMessageTypeDef]
    ) -> CreateDBClusterResultTypeDef:
        """
        Creates a new Amazon Aurora DB cluster or Multi-AZ DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/create_db_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_cluster)
        """

    def create_db_cluster_endpoint(
        self, **kwargs: Unpack[CreateDBClusterEndpointMessageTypeDef]
    ) -> DBClusterEndpointResponseTypeDef:
        """
        Creates a new custom endpoint and associates it with an Amazon Aurora DB
        cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/create_db_cluster_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_cluster_endpoint)
        """

    def create_db_cluster_parameter_group(
        self, **kwargs: Unpack[CreateDBClusterParameterGroupMessageTypeDef]
    ) -> CreateDBClusterParameterGroupResultTypeDef:
        """
        Creates a new DB cluster parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/create_db_cluster_parameter_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_cluster_parameter_group)
        """

    def create_db_cluster_snapshot(
        self, **kwargs: Unpack[CreateDBClusterSnapshotMessageTypeDef]
    ) -> CreateDBClusterSnapshotResultTypeDef:
        """
        Creates a snapshot of a DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/create_db_cluster_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_cluster_snapshot)
        """

    def create_db_instance(
        self, **kwargs: Unpack[CreateDBInstanceMessageTypeDef]
    ) -> CreateDBInstanceResultTypeDef:
        """
        Creates a new DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/create_db_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_instance)
        """

    def create_db_instance_read_replica(
        self, **kwargs: Unpack[CreateDBInstanceReadReplicaMessageTypeDef]
    ) -> CreateDBInstanceReadReplicaResultTypeDef:
        """
        Creates a new DB instance that acts as a read replica for an existing source DB
        instance or Multi-AZ DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/create_db_instance_read_replica.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_instance_read_replica)
        """

    def create_db_parameter_group(
        self, **kwargs: Unpack[CreateDBParameterGroupMessageTypeDef]
    ) -> CreateDBParameterGroupResultTypeDef:
        """
        Creates a new DB parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/create_db_parameter_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_parameter_group)
        """

    def create_db_proxy(
        self, **kwargs: Unpack[CreateDBProxyRequestTypeDef]
    ) -> CreateDBProxyResponseTypeDef:
        """
        Creates a new DB proxy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/create_db_proxy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_proxy)
        """

    def create_db_proxy_endpoint(
        self, **kwargs: Unpack[CreateDBProxyEndpointRequestTypeDef]
    ) -> CreateDBProxyEndpointResponseTypeDef:
        """
        Creates a <code>DBProxyEndpoint</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/create_db_proxy_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_proxy_endpoint)
        """

    def create_db_security_group(
        self, **kwargs: Unpack[CreateDBSecurityGroupMessageTypeDef]
    ) -> CreateDBSecurityGroupResultTypeDef:
        """
        Creates a new DB security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/create_db_security_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_security_group)
        """

    def create_db_shard_group(
        self, **kwargs: Unpack[CreateDBShardGroupMessageTypeDef]
    ) -> DBShardGroupResponseTypeDef:
        """
        Creates a new DB shard group for Aurora Limitless Database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/create_db_shard_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_shard_group)
        """

    def create_db_snapshot(
        self, **kwargs: Unpack[CreateDBSnapshotMessageTypeDef]
    ) -> CreateDBSnapshotResultTypeDef:
        """
        Creates a snapshot of a DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/create_db_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_snapshot)
        """

    def create_db_subnet_group(
        self, **kwargs: Unpack[CreateDBSubnetGroupMessageTypeDef]
    ) -> CreateDBSubnetGroupResultTypeDef:
        """
        Creates a new DB subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/create_db_subnet_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_subnet_group)
        """

    def create_event_subscription(
        self, **kwargs: Unpack[CreateEventSubscriptionMessageTypeDef]
    ) -> CreateEventSubscriptionResultTypeDef:
        """
        Creates an RDS event notification subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/create_event_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_event_subscription)
        """

    def create_global_cluster(
        self, **kwargs: Unpack[CreateGlobalClusterMessageTypeDef]
    ) -> CreateGlobalClusterResultTypeDef:
        """
        Creates an Aurora global database spread across multiple Amazon Web Services
        Regions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/create_global_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_global_cluster)
        """

    def create_integration(
        self, **kwargs: Unpack[CreateIntegrationMessageTypeDef]
    ) -> IntegrationResponseTypeDef:
        """
        Creates a zero-ETL integration with Amazon Redshift.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/create_integration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_integration)
        """

    def create_option_group(
        self, **kwargs: Unpack[CreateOptionGroupMessageTypeDef]
    ) -> CreateOptionGroupResultTypeDef:
        """
        Creates a new option group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/create_option_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_option_group)
        """

    def create_tenant_database(
        self, **kwargs: Unpack[CreateTenantDatabaseMessageTypeDef]
    ) -> CreateTenantDatabaseResultTypeDef:
        """
        Creates a tenant database in a DB instance that uses the multi-tenant
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/create_tenant_database.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_tenant_database)
        """

    def delete_blue_green_deployment(
        self, **kwargs: Unpack[DeleteBlueGreenDeploymentRequestTypeDef]
    ) -> DeleteBlueGreenDeploymentResponseTypeDef:
        """
        Deletes a blue/green deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/delete_blue_green_deployment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_blue_green_deployment)
        """

    def delete_custom_db_engine_version(
        self, **kwargs: Unpack[DeleteCustomDBEngineVersionMessageTypeDef]
    ) -> DBEngineVersionResponseTypeDef:
        """
        Deletes a custom engine version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/delete_custom_db_engine_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_custom_db_engine_version)
        """

    def delete_db_cluster(
        self, **kwargs: Unpack[DeleteDBClusterMessageTypeDef]
    ) -> DeleteDBClusterResultTypeDef:
        """
        The DeleteDBCluster action deletes a previously provisioned DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/delete_db_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_cluster)
        """

    def delete_db_cluster_automated_backup(
        self, **kwargs: Unpack[DeleteDBClusterAutomatedBackupMessageTypeDef]
    ) -> DeleteDBClusterAutomatedBackupResultTypeDef:
        """
        Deletes automated backups using the <code>DbClusterResourceId</code> value of
        the source DB cluster or the Amazon Resource Name (ARN) of the automated
        backups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/delete_db_cluster_automated_backup.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_cluster_automated_backup)
        """

    def delete_db_cluster_endpoint(
        self, **kwargs: Unpack[DeleteDBClusterEndpointMessageTypeDef]
    ) -> DBClusterEndpointResponseTypeDef:
        """
        Deletes a custom endpoint and removes it from an Amazon Aurora DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/delete_db_cluster_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_cluster_endpoint)
        """

    def delete_db_cluster_parameter_group(
        self, **kwargs: Unpack[DeleteDBClusterParameterGroupMessageTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a specified DB cluster parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/delete_db_cluster_parameter_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_cluster_parameter_group)
        """

    def delete_db_cluster_snapshot(
        self, **kwargs: Unpack[DeleteDBClusterSnapshotMessageTypeDef]
    ) -> DeleteDBClusterSnapshotResultTypeDef:
        """
        Deletes a DB cluster snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/delete_db_cluster_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_cluster_snapshot)
        """

    def delete_db_instance(
        self, **kwargs: Unpack[DeleteDBInstanceMessageTypeDef]
    ) -> DeleteDBInstanceResultTypeDef:
        """
        Deletes a previously provisioned DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/delete_db_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_instance)
        """

    def delete_db_instance_automated_backup(
        self, **kwargs: Unpack[DeleteDBInstanceAutomatedBackupMessageTypeDef]
    ) -> DeleteDBInstanceAutomatedBackupResultTypeDef:
        """
        Deletes automated backups using the <code>DbiResourceId</code> value of the
        source DB instance or the Amazon Resource Name (ARN) of the automated backups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/delete_db_instance_automated_backup.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_instance_automated_backup)
        """

    def delete_db_parameter_group(
        self, **kwargs: Unpack[DeleteDBParameterGroupMessageTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a specified DB parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/delete_db_parameter_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_parameter_group)
        """

    def delete_db_proxy(
        self, **kwargs: Unpack[DeleteDBProxyRequestTypeDef]
    ) -> DeleteDBProxyResponseTypeDef:
        """
        Deletes an existing DB proxy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/delete_db_proxy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_proxy)
        """

    def delete_db_proxy_endpoint(
        self, **kwargs: Unpack[DeleteDBProxyEndpointRequestTypeDef]
    ) -> DeleteDBProxyEndpointResponseTypeDef:
        """
        Deletes a <code>DBProxyEndpoint</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/delete_db_proxy_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_proxy_endpoint)
        """

    def delete_db_security_group(
        self, **kwargs: Unpack[DeleteDBSecurityGroupMessageTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a DB security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/delete_db_security_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_security_group)
        """

    def delete_db_shard_group(
        self, **kwargs: Unpack[DeleteDBShardGroupMessageTypeDef]
    ) -> DBShardGroupResponseTypeDef:
        """
        Deletes an Aurora Limitless Database DB shard group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/delete_db_shard_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_shard_group)
        """

    def delete_db_snapshot(
        self, **kwargs: Unpack[DeleteDBSnapshotMessageTypeDef]
    ) -> DeleteDBSnapshotResultTypeDef:
        """
        Deletes a DB snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/delete_db_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_snapshot)
        """

    def delete_db_subnet_group(
        self, **kwargs: Unpack[DeleteDBSubnetGroupMessageTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a DB subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/delete_db_subnet_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_subnet_group)
        """

    def delete_event_subscription(
        self, **kwargs: Unpack[DeleteEventSubscriptionMessageTypeDef]
    ) -> DeleteEventSubscriptionResultTypeDef:
        """
        Deletes an RDS event notification subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/delete_event_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_event_subscription)
        """

    def delete_global_cluster(
        self, **kwargs: Unpack[DeleteGlobalClusterMessageTypeDef]
    ) -> DeleteGlobalClusterResultTypeDef:
        """
        Deletes a global database cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/delete_global_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_global_cluster)
        """

    def delete_integration(
        self, **kwargs: Unpack[DeleteIntegrationMessageTypeDef]
    ) -> IntegrationResponseTypeDef:
        """
        Deletes a zero-ETL integration with Amazon Redshift.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/delete_integration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_integration)
        """

    def delete_option_group(
        self, **kwargs: Unpack[DeleteOptionGroupMessageTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an existing option group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/delete_option_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_option_group)
        """

    def delete_tenant_database(
        self, **kwargs: Unpack[DeleteTenantDatabaseMessageTypeDef]
    ) -> DeleteTenantDatabaseResultTypeDef:
        """
        Deletes a tenant database from your DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/delete_tenant_database.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_tenant_database)
        """

    def deregister_db_proxy_targets(
        self, **kwargs: Unpack[DeregisterDBProxyTargetsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Remove the association between one or more <code>DBProxyTarget</code> data
        structures and a <code>DBProxyTargetGroup</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/deregister_db_proxy_targets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#deregister_db_proxy_targets)
        """

    def describe_account_attributes(self) -> AccountAttributesMessageTypeDef:
        """
        Lists all of the attributes for a customer account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_account_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_account_attributes)
        """

    def describe_blue_green_deployments(
        self, **kwargs: Unpack[DescribeBlueGreenDeploymentsRequestTypeDef]
    ) -> DescribeBlueGreenDeploymentsResponseTypeDef:
        """
        Describes one or more blue/green deployments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_blue_green_deployments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_blue_green_deployments)
        """

    def describe_certificates(
        self, **kwargs: Unpack[DescribeCertificatesMessageTypeDef]
    ) -> CertificateMessageTypeDef:
        """
        Lists the set of certificate authority (CA) certificates provided by Amazon RDS
        for this Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_certificates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_certificates)
        """

    def describe_db_cluster_automated_backups(
        self, **kwargs: Unpack[DescribeDBClusterAutomatedBackupsMessageTypeDef]
    ) -> DBClusterAutomatedBackupMessageTypeDef:
        """
        Displays backups for both current and deleted DB clusters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_db_cluster_automated_backups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_cluster_automated_backups)
        """

    def describe_db_cluster_backtracks(
        self, **kwargs: Unpack[DescribeDBClusterBacktracksMessageTypeDef]
    ) -> DBClusterBacktrackMessageTypeDef:
        """
        Returns information about backtracks for a DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_db_cluster_backtracks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_cluster_backtracks)
        """

    def describe_db_cluster_endpoints(
        self, **kwargs: Unpack[DescribeDBClusterEndpointsMessageTypeDef]
    ) -> DBClusterEndpointMessageTypeDef:
        """
        Returns information about endpoints for an Amazon Aurora DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_db_cluster_endpoints.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_cluster_endpoints)
        """

    def describe_db_cluster_parameter_groups(
        self, **kwargs: Unpack[DescribeDBClusterParameterGroupsMessageTypeDef]
    ) -> DBClusterParameterGroupsMessageTypeDef:
        """
        Returns a list of <code>DBClusterParameterGroup</code> descriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_db_cluster_parameter_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_cluster_parameter_groups)
        """

    def describe_db_cluster_parameters(
        self, **kwargs: Unpack[DescribeDBClusterParametersMessageTypeDef]
    ) -> DBClusterParameterGroupDetailsTypeDef:
        """
        Returns the detailed parameter list for a particular DB cluster parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_db_cluster_parameters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_cluster_parameters)
        """

    def describe_db_cluster_snapshot_attributes(
        self, **kwargs: Unpack[DescribeDBClusterSnapshotAttributesMessageTypeDef]
    ) -> DescribeDBClusterSnapshotAttributesResultTypeDef:
        """
        Returns a list of DB cluster snapshot attribute names and values for a manual
        DB cluster snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_db_cluster_snapshot_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_cluster_snapshot_attributes)
        """

    def describe_db_cluster_snapshots(
        self, **kwargs: Unpack[DescribeDBClusterSnapshotsMessageTypeDef]
    ) -> DBClusterSnapshotMessageTypeDef:
        """
        Returns information about DB cluster snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_db_cluster_snapshots.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_cluster_snapshots)
        """

    def describe_db_clusters(
        self, **kwargs: Unpack[DescribeDBClustersMessageTypeDef]
    ) -> DBClusterMessageTypeDef:
        """
        Describes existing Amazon Aurora DB clusters and Multi-AZ DB clusters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_db_clusters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_clusters)
        """

    def describe_db_engine_versions(
        self, **kwargs: Unpack[DescribeDBEngineVersionsMessageTypeDef]
    ) -> DBEngineVersionMessageTypeDef:
        """
        Describes the properties of specific versions of DB engines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_db_engine_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_engine_versions)
        """

    def describe_db_instance_automated_backups(
        self, **kwargs: Unpack[DescribeDBInstanceAutomatedBackupsMessageTypeDef]
    ) -> DBInstanceAutomatedBackupMessageTypeDef:
        """
        Displays backups for both current and deleted instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_db_instance_automated_backups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_instance_automated_backups)
        """

    def describe_db_instances(
        self, **kwargs: Unpack[DescribeDBInstancesMessageTypeDef]
    ) -> DBInstanceMessageTypeDef:
        """
        Describes provisioned RDS instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_db_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_instances)
        """

    def describe_db_log_files(
        self, **kwargs: Unpack[DescribeDBLogFilesMessageTypeDef]
    ) -> DescribeDBLogFilesResponseTypeDef:
        """
        Returns a list of DB log files for the DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_db_log_files.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_log_files)
        """

    def describe_db_parameter_groups(
        self, **kwargs: Unpack[DescribeDBParameterGroupsMessageTypeDef]
    ) -> DBParameterGroupsMessageTypeDef:
        """
        Returns a list of <code>DBParameterGroup</code> descriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_db_parameter_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_parameter_groups)
        """

    def describe_db_parameters(
        self, **kwargs: Unpack[DescribeDBParametersMessageTypeDef]
    ) -> DBParameterGroupDetailsTypeDef:
        """
        Returns the detailed parameter list for a particular DB parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_db_parameters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_parameters)
        """

    def describe_db_proxies(
        self, **kwargs: Unpack[DescribeDBProxiesRequestTypeDef]
    ) -> DescribeDBProxiesResponseTypeDef:
        """
        Returns information about DB proxies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_db_proxies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_proxies)
        """

    def describe_db_proxy_endpoints(
        self, **kwargs: Unpack[DescribeDBProxyEndpointsRequestTypeDef]
    ) -> DescribeDBProxyEndpointsResponseTypeDef:
        """
        Returns information about DB proxy endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_db_proxy_endpoints.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_proxy_endpoints)
        """

    def describe_db_proxy_target_groups(
        self, **kwargs: Unpack[DescribeDBProxyTargetGroupsRequestTypeDef]
    ) -> DescribeDBProxyTargetGroupsResponseTypeDef:
        """
        Returns information about DB proxy target groups, represented by
        <code>DBProxyTargetGroup</code> data structures.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_db_proxy_target_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_proxy_target_groups)
        """

    def describe_db_proxy_targets(
        self, **kwargs: Unpack[DescribeDBProxyTargetsRequestTypeDef]
    ) -> DescribeDBProxyTargetsResponseTypeDef:
        """
        Returns information about <code>DBProxyTarget</code> objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_db_proxy_targets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_proxy_targets)
        """

    def describe_db_recommendations(
        self, **kwargs: Unpack[DescribeDBRecommendationsMessageTypeDef]
    ) -> DBRecommendationsMessageTypeDef:
        """
        Describes the recommendations to resolve the issues for your DB instances, DB
        clusters, and DB parameter groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_db_recommendations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_recommendations)
        """

    def describe_db_security_groups(
        self, **kwargs: Unpack[DescribeDBSecurityGroupsMessageTypeDef]
    ) -> DBSecurityGroupMessageTypeDef:
        """
        Returns a list of <code>DBSecurityGroup</code> descriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_db_security_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_security_groups)
        """

    def describe_db_shard_groups(
        self, **kwargs: Unpack[DescribeDBShardGroupsMessageTypeDef]
    ) -> DescribeDBShardGroupsResponseTypeDef:
        """
        Describes existing Aurora Limitless Database DB shard groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_db_shard_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_shard_groups)
        """

    def describe_db_snapshot_attributes(
        self, **kwargs: Unpack[DescribeDBSnapshotAttributesMessageTypeDef]
    ) -> DescribeDBSnapshotAttributesResultTypeDef:
        """
        Returns a list of DB snapshot attribute names and values for a manual DB
        snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_db_snapshot_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_snapshot_attributes)
        """

    def describe_db_snapshot_tenant_databases(
        self, **kwargs: Unpack[DescribeDBSnapshotTenantDatabasesMessageTypeDef]
    ) -> DBSnapshotTenantDatabasesMessageTypeDef:
        """
        Describes the tenant databases that exist in a DB snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_db_snapshot_tenant_databases.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_snapshot_tenant_databases)
        """

    def describe_db_snapshots(
        self, **kwargs: Unpack[DescribeDBSnapshotsMessageTypeDef]
    ) -> DBSnapshotMessageTypeDef:
        """
        Returns information about DB snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_db_snapshots.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_snapshots)
        """

    def describe_db_subnet_groups(
        self, **kwargs: Unpack[DescribeDBSubnetGroupsMessageTypeDef]
    ) -> DBSubnetGroupMessageTypeDef:
        """
        Returns a list of DBSubnetGroup descriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_db_subnet_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_subnet_groups)
        """

    def describe_engine_default_cluster_parameters(
        self, **kwargs: Unpack[DescribeEngineDefaultClusterParametersMessageTypeDef]
    ) -> DescribeEngineDefaultClusterParametersResultTypeDef:
        """
        Returns the default engine and system parameter information for the cluster
        database engine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_engine_default_cluster_parameters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_engine_default_cluster_parameters)
        """

    def describe_engine_default_parameters(
        self, **kwargs: Unpack[DescribeEngineDefaultParametersMessageTypeDef]
    ) -> DescribeEngineDefaultParametersResultTypeDef:
        """
        Returns the default engine and system parameter information for the specified
        database engine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_engine_default_parameters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_engine_default_parameters)
        """

    def describe_event_categories(
        self, **kwargs: Unpack[DescribeEventCategoriesMessageTypeDef]
    ) -> EventCategoriesMessageTypeDef:
        """
        Displays a list of categories for all event source types, or, if specified, for
        a specified source type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_event_categories.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_event_categories)
        """

    def describe_event_subscriptions(
        self, **kwargs: Unpack[DescribeEventSubscriptionsMessageTypeDef]
    ) -> EventSubscriptionsMessageTypeDef:
        """
        Lists all the subscription descriptions for a customer account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_event_subscriptions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_event_subscriptions)
        """

    def describe_events(
        self, **kwargs: Unpack[DescribeEventsMessageTypeDef]
    ) -> EventsMessageTypeDef:
        """
        Returns events related to DB instances, DB clusters, DB parameter groups, DB
        security groups, DB snapshots, DB cluster snapshots, and RDS Proxies for the
        past 14 days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_events.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_events)
        """

    def describe_export_tasks(
        self, **kwargs: Unpack[DescribeExportTasksMessageTypeDef]
    ) -> ExportTasksMessageTypeDef:
        """
        Returns information about a snapshot or cluster export to Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_export_tasks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_export_tasks)
        """

    def describe_global_clusters(
        self, **kwargs: Unpack[DescribeGlobalClustersMessageTypeDef]
    ) -> GlobalClustersMessageTypeDef:
        """
        Returns information about Aurora global database clusters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_global_clusters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_global_clusters)
        """

    def describe_integrations(
        self, **kwargs: Unpack[DescribeIntegrationsMessageTypeDef]
    ) -> DescribeIntegrationsResponseTypeDef:
        """
        Describe one or more zero-ETL integrations with Amazon Redshift.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_integrations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_integrations)
        """

    def describe_option_group_options(
        self, **kwargs: Unpack[DescribeOptionGroupOptionsMessageTypeDef]
    ) -> OptionGroupOptionsMessageTypeDef:
        """
        Describes all available options for the specified engine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_option_group_options.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_option_group_options)
        """

    def describe_option_groups(
        self, **kwargs: Unpack[DescribeOptionGroupsMessageTypeDef]
    ) -> OptionGroupsTypeDef:
        """
        Describes the available option groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_option_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_option_groups)
        """

    def describe_orderable_db_instance_options(
        self, **kwargs: Unpack[DescribeOrderableDBInstanceOptionsMessageTypeDef]
    ) -> OrderableDBInstanceOptionsMessageTypeDef:
        """
        Describes the orderable DB instance options for a specified DB engine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_orderable_db_instance_options.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_orderable_db_instance_options)
        """

    def describe_pending_maintenance_actions(
        self, **kwargs: Unpack[DescribePendingMaintenanceActionsMessageTypeDef]
    ) -> PendingMaintenanceActionsMessageTypeDef:
        """
        Returns a list of resources (for example, DB instances) that have at least one
        pending maintenance action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_pending_maintenance_actions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_pending_maintenance_actions)
        """

    def describe_reserved_db_instances(
        self, **kwargs: Unpack[DescribeReservedDBInstancesMessageTypeDef]
    ) -> ReservedDBInstanceMessageTypeDef:
        """
        Returns information about reserved DB instances for this account, or about a
        specified reserved DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_reserved_db_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_reserved_db_instances)
        """

    def describe_reserved_db_instances_offerings(
        self, **kwargs: Unpack[DescribeReservedDBInstancesOfferingsMessageTypeDef]
    ) -> ReservedDBInstancesOfferingMessageTypeDef:
        """
        Lists available reserved DB instance offerings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_reserved_db_instances_offerings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_reserved_db_instances_offerings)
        """

    def describe_source_regions(
        self, **kwargs: Unpack[DescribeSourceRegionsMessageTypeDef]
    ) -> SourceRegionMessageTypeDef:
        """
        Returns a list of the source Amazon Web Services Regions where the current
        Amazon Web Services Region can create a read replica, copy a DB snapshot from,
        or replicate automated backups from.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_source_regions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_source_regions)
        """

    def describe_tenant_databases(
        self, **kwargs: Unpack[DescribeTenantDatabasesMessageTypeDef]
    ) -> TenantDatabasesMessageTypeDef:
        """
        Describes the tenant databases in a DB instance that uses the multi-tenant
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_tenant_databases.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_tenant_databases)
        """

    def describe_valid_db_instance_modifications(
        self, **kwargs: Unpack[DescribeValidDBInstanceModificationsMessageTypeDef]
    ) -> DescribeValidDBInstanceModificationsResultTypeDef:
        """
        You can call <code>DescribeValidDBInstanceModifications</code> to learn what
        modifications you can make to your DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_valid_db_instance_modifications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_valid_db_instance_modifications)
        """

    def disable_http_endpoint(
        self, **kwargs: Unpack[DisableHttpEndpointRequestTypeDef]
    ) -> DisableHttpEndpointResponseTypeDef:
        """
        Disables the HTTP endpoint for the specified DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/disable_http_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#disable_http_endpoint)
        """

    def download_db_log_file_portion(
        self, **kwargs: Unpack[DownloadDBLogFilePortionMessageTypeDef]
    ) -> DownloadDBLogFilePortionDetailsTypeDef:
        """
        Downloads all or a portion of the specified log file, up to 1 MB in size.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/download_db_log_file_portion.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#download_db_log_file_portion)
        """

    def enable_http_endpoint(
        self, **kwargs: Unpack[EnableHttpEndpointRequestTypeDef]
    ) -> EnableHttpEndpointResponseTypeDef:
        """
        Enables the HTTP endpoint for the DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/enable_http_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#enable_http_endpoint)
        """

    def failover_db_cluster(
        self, **kwargs: Unpack[FailoverDBClusterMessageTypeDef]
    ) -> FailoverDBClusterResultTypeDef:
        """
        Forces a failover for a DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/failover_db_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#failover_db_cluster)
        """

    def failover_global_cluster(
        self, **kwargs: Unpack[FailoverGlobalClusterMessageTypeDef]
    ) -> FailoverGlobalClusterResultTypeDef:
        """
        Promotes the specified secondary DB cluster to be the primary DB cluster in the
        global database cluster to fail over or switch over a global database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/failover_global_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#failover_global_cluster)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceMessageTypeDef]
    ) -> TagListMessageTypeDef:
        """
        Lists all tags on an Amazon RDS resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#list_tags_for_resource)
        """

    def modify_activity_stream(
        self, **kwargs: Unpack[ModifyActivityStreamRequestTypeDef]
    ) -> ModifyActivityStreamResponseTypeDef:
        """
        Changes the audit policy state of a database activity stream to either locked
        (default) or unlocked.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/modify_activity_stream.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_activity_stream)
        """

    def modify_certificates(
        self, **kwargs: Unpack[ModifyCertificatesMessageTypeDef]
    ) -> ModifyCertificatesResultTypeDef:
        """
        Override the system-default Secure Sockets Layer/Transport Layer Security
        (SSL/TLS) certificate for Amazon RDS for new DB instances, or remove the
        override.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/modify_certificates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_certificates)
        """

    def modify_current_db_cluster_capacity(
        self, **kwargs: Unpack[ModifyCurrentDBClusterCapacityMessageTypeDef]
    ) -> DBClusterCapacityInfoTypeDef:
        """
        Set the capacity of an Aurora Serverless v1 DB cluster to a specific value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/modify_current_db_cluster_capacity.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_current_db_cluster_capacity)
        """

    def modify_custom_db_engine_version(
        self, **kwargs: Unpack[ModifyCustomDBEngineVersionMessageTypeDef]
    ) -> DBEngineVersionResponseTypeDef:
        """
        Modifies the status of a custom engine version (CEV).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/modify_custom_db_engine_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_custom_db_engine_version)
        """

    def modify_db_cluster(
        self, **kwargs: Unpack[ModifyDBClusterMessageTypeDef]
    ) -> ModifyDBClusterResultTypeDef:
        """
        Modifies the settings of an Amazon Aurora DB cluster or a Multi-AZ DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/modify_db_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_cluster)
        """

    def modify_db_cluster_endpoint(
        self, **kwargs: Unpack[ModifyDBClusterEndpointMessageTypeDef]
    ) -> DBClusterEndpointResponseTypeDef:
        """
        Modifies the properties of an endpoint in an Amazon Aurora DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/modify_db_cluster_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_cluster_endpoint)
        """

    def modify_db_cluster_parameter_group(
        self, **kwargs: Unpack[ModifyDBClusterParameterGroupMessageTypeDef]
    ) -> DBClusterParameterGroupNameMessageTypeDef:
        """
        Modifies the parameters of a DB cluster parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/modify_db_cluster_parameter_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_cluster_parameter_group)
        """

    def modify_db_cluster_snapshot_attribute(
        self, **kwargs: Unpack[ModifyDBClusterSnapshotAttributeMessageTypeDef]
    ) -> ModifyDBClusterSnapshotAttributeResultTypeDef:
        """
        Adds an attribute and values to, or removes an attribute and values from, a
        manual DB cluster snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/modify_db_cluster_snapshot_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_cluster_snapshot_attribute)
        """

    def modify_db_instance(
        self, **kwargs: Unpack[ModifyDBInstanceMessageTypeDef]
    ) -> ModifyDBInstanceResultTypeDef:
        """
        Modifies settings for a DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/modify_db_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_instance)
        """

    def modify_db_parameter_group(
        self, **kwargs: Unpack[ModifyDBParameterGroupMessageTypeDef]
    ) -> DBParameterGroupNameMessageTypeDef:
        """
        Modifies the parameters of a DB parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/modify_db_parameter_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_parameter_group)
        """

    def modify_db_proxy(
        self, **kwargs: Unpack[ModifyDBProxyRequestTypeDef]
    ) -> ModifyDBProxyResponseTypeDef:
        """
        Changes the settings for an existing DB proxy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/modify_db_proxy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_proxy)
        """

    def modify_db_proxy_endpoint(
        self, **kwargs: Unpack[ModifyDBProxyEndpointRequestTypeDef]
    ) -> ModifyDBProxyEndpointResponseTypeDef:
        """
        Changes the settings for an existing DB proxy endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/modify_db_proxy_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_proxy_endpoint)
        """

    def modify_db_proxy_target_group(
        self, **kwargs: Unpack[ModifyDBProxyTargetGroupRequestTypeDef]
    ) -> ModifyDBProxyTargetGroupResponseTypeDef:
        """
        Modifies the properties of a <code>DBProxyTargetGroup</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/modify_db_proxy_target_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_proxy_target_group)
        """

    def modify_db_recommendation(
        self, **kwargs: Unpack[ModifyDBRecommendationMessageTypeDef]
    ) -> DBRecommendationMessageTypeDef:
        """
        Updates the recommendation status and recommended action status for the
        specified recommendation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/modify_db_recommendation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_recommendation)
        """

    def modify_db_shard_group(
        self, **kwargs: Unpack[ModifyDBShardGroupMessageTypeDef]
    ) -> DBShardGroupResponseTypeDef:
        """
        Modifies the settings of an Aurora Limitless Database DB shard group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/modify_db_shard_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_shard_group)
        """

    def modify_db_snapshot(
        self, **kwargs: Unpack[ModifyDBSnapshotMessageTypeDef]
    ) -> ModifyDBSnapshotResultTypeDef:
        """
        Updates a manual DB snapshot with a new engine version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/modify_db_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_snapshot)
        """

    def modify_db_snapshot_attribute(
        self, **kwargs: Unpack[ModifyDBSnapshotAttributeMessageTypeDef]
    ) -> ModifyDBSnapshotAttributeResultTypeDef:
        """
        Adds an attribute and values to, or removes an attribute and values from, a
        manual DB snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/modify_db_snapshot_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_snapshot_attribute)
        """

    def modify_db_subnet_group(
        self, **kwargs: Unpack[ModifyDBSubnetGroupMessageTypeDef]
    ) -> ModifyDBSubnetGroupResultTypeDef:
        """
        Modifies an existing DB subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/modify_db_subnet_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_subnet_group)
        """

    def modify_event_subscription(
        self, **kwargs: Unpack[ModifyEventSubscriptionMessageTypeDef]
    ) -> ModifyEventSubscriptionResultTypeDef:
        """
        Modifies an existing RDS event notification subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/modify_event_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_event_subscription)
        """

    def modify_global_cluster(
        self, **kwargs: Unpack[ModifyGlobalClusterMessageTypeDef]
    ) -> ModifyGlobalClusterResultTypeDef:
        """
        Modifies a setting for an Amazon Aurora global database cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/modify_global_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_global_cluster)
        """

    def modify_integration(
        self, **kwargs: Unpack[ModifyIntegrationMessageTypeDef]
    ) -> IntegrationResponseTypeDef:
        """
        Modifies a zero-ETL integration with Amazon Redshift.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/modify_integration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_integration)
        """

    def modify_option_group(
        self, **kwargs: Unpack[ModifyOptionGroupMessageTypeDef]
    ) -> ModifyOptionGroupResultTypeDef:
        """
        Modifies an existing option group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/modify_option_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_option_group)
        """

    def modify_tenant_database(
        self, **kwargs: Unpack[ModifyTenantDatabaseMessageTypeDef]
    ) -> ModifyTenantDatabaseResultTypeDef:
        """
        Modifies an existing tenant database in a DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/modify_tenant_database.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_tenant_database)
        """

    def promote_read_replica(
        self, **kwargs: Unpack[PromoteReadReplicaMessageTypeDef]
    ) -> PromoteReadReplicaResultTypeDef:
        """
        Promotes a read replica DB instance to a standalone DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/promote_read_replica.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#promote_read_replica)
        """

    def promote_read_replica_db_cluster(
        self, **kwargs: Unpack[PromoteReadReplicaDBClusterMessageTypeDef]
    ) -> PromoteReadReplicaDBClusterResultTypeDef:
        """
        Promotes a read replica DB cluster to a standalone DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/promote_read_replica_db_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#promote_read_replica_db_cluster)
        """

    def purchase_reserved_db_instances_offering(
        self, **kwargs: Unpack[PurchaseReservedDBInstancesOfferingMessageTypeDef]
    ) -> PurchaseReservedDBInstancesOfferingResultTypeDef:
        """
        Purchases a reserved DB instance offering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/purchase_reserved_db_instances_offering.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#purchase_reserved_db_instances_offering)
        """

    def reboot_db_cluster(
        self, **kwargs: Unpack[RebootDBClusterMessageTypeDef]
    ) -> RebootDBClusterResultTypeDef:
        """
        You might need to reboot your DB cluster, usually for maintenance reasons.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/reboot_db_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#reboot_db_cluster)
        """

    def reboot_db_instance(
        self, **kwargs: Unpack[RebootDBInstanceMessageTypeDef]
    ) -> RebootDBInstanceResultTypeDef:
        """
        You might need to reboot your DB instance, usually for maintenance reasons.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/reboot_db_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#reboot_db_instance)
        """

    def reboot_db_shard_group(
        self, **kwargs: Unpack[RebootDBShardGroupMessageTypeDef]
    ) -> DBShardGroupResponseTypeDef:
        """
        You might need to reboot your DB shard group, usually for maintenance reasons.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/reboot_db_shard_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#reboot_db_shard_group)
        """

    def register_db_proxy_targets(
        self, **kwargs: Unpack[RegisterDBProxyTargetsRequestTypeDef]
    ) -> RegisterDBProxyTargetsResponseTypeDef:
        """
        Associate one or more <code>DBProxyTarget</code> data structures with a
        <code>DBProxyTargetGroup</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/register_db_proxy_targets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#register_db_proxy_targets)
        """

    def remove_from_global_cluster(
        self, **kwargs: Unpack[RemoveFromGlobalClusterMessageTypeDef]
    ) -> RemoveFromGlobalClusterResultTypeDef:
        """
        Detaches an Aurora secondary cluster from an Aurora global database cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/remove_from_global_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#remove_from_global_cluster)
        """

    def remove_role_from_db_cluster(
        self, **kwargs: Unpack[RemoveRoleFromDBClusterMessageTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes the asssociation of an Amazon Web Services Identity and Access
        Management (IAM) role from a DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/remove_role_from_db_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#remove_role_from_db_cluster)
        """

    def remove_role_from_db_instance(
        self, **kwargs: Unpack[RemoveRoleFromDBInstanceMessageTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Disassociates an Amazon Web Services Identity and Access Management (IAM) role
        from a DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/remove_role_from_db_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#remove_role_from_db_instance)
        """

    def remove_source_identifier_from_subscription(
        self, **kwargs: Unpack[RemoveSourceIdentifierFromSubscriptionMessageTypeDef]
    ) -> RemoveSourceIdentifierFromSubscriptionResultTypeDef:
        """
        Removes a source identifier from an existing RDS event notification
        subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/remove_source_identifier_from_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#remove_source_identifier_from_subscription)
        """

    def remove_tags_from_resource(
        self, **kwargs: Unpack[RemoveTagsFromResourceMessageTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes metadata tags from an Amazon RDS resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/remove_tags_from_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#remove_tags_from_resource)
        """

    def reset_db_cluster_parameter_group(
        self, **kwargs: Unpack[ResetDBClusterParameterGroupMessageTypeDef]
    ) -> DBClusterParameterGroupNameMessageTypeDef:
        """
        Modifies the parameters of a DB cluster parameter group to the default value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/reset_db_cluster_parameter_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#reset_db_cluster_parameter_group)
        """

    def reset_db_parameter_group(
        self, **kwargs: Unpack[ResetDBParameterGroupMessageTypeDef]
    ) -> DBParameterGroupNameMessageTypeDef:
        """
        Modifies the parameters of a DB parameter group to the engine/system default
        value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/reset_db_parameter_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#reset_db_parameter_group)
        """

    def restore_db_cluster_from_s3(
        self, **kwargs: Unpack[RestoreDBClusterFromS3MessageTypeDef]
    ) -> RestoreDBClusterFromS3ResultTypeDef:
        """
        Creates an Amazon Aurora DB cluster from MySQL data stored in an Amazon S3
        bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/restore_db_cluster_from_s3.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#restore_db_cluster_from_s3)
        """

    def restore_db_cluster_from_snapshot(
        self, **kwargs: Unpack[RestoreDBClusterFromSnapshotMessageTypeDef]
    ) -> RestoreDBClusterFromSnapshotResultTypeDef:
        """
        Creates a new DB cluster from a DB snapshot or DB cluster snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/restore_db_cluster_from_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#restore_db_cluster_from_snapshot)
        """

    def restore_db_cluster_to_point_in_time(
        self, **kwargs: Unpack[RestoreDBClusterToPointInTimeMessageTypeDef]
    ) -> RestoreDBClusterToPointInTimeResultTypeDef:
        """
        Restores a DB cluster to an arbitrary point in time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/restore_db_cluster_to_point_in_time.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#restore_db_cluster_to_point_in_time)
        """

    def restore_db_instance_from_db_snapshot(
        self, **kwargs: Unpack[RestoreDBInstanceFromDBSnapshotMessageTypeDef]
    ) -> RestoreDBInstanceFromDBSnapshotResultTypeDef:
        """
        Creates a new DB instance from a DB snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/restore_db_instance_from_db_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#restore_db_instance_from_db_snapshot)
        """

    def restore_db_instance_from_s3(
        self, **kwargs: Unpack[RestoreDBInstanceFromS3MessageTypeDef]
    ) -> RestoreDBInstanceFromS3ResultTypeDef:
        """
        Amazon Relational Database Service (Amazon RDS) supports importing MySQL
        databases by using backup files.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/restore_db_instance_from_s3.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#restore_db_instance_from_s3)
        """

    def restore_db_instance_to_point_in_time(
        self, **kwargs: Unpack[RestoreDBInstanceToPointInTimeMessageTypeDef]
    ) -> RestoreDBInstanceToPointInTimeResultTypeDef:
        """
        Restores a DB instance to an arbitrary point in time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/restore_db_instance_to_point_in_time.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#restore_db_instance_to_point_in_time)
        """

    def revoke_db_security_group_ingress(
        self, **kwargs: Unpack[RevokeDBSecurityGroupIngressMessageTypeDef]
    ) -> RevokeDBSecurityGroupIngressResultTypeDef:
        """
        Revokes ingress from a DBSecurityGroup for previously authorized IP ranges or
        EC2 or VPC security groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/revoke_db_security_group_ingress.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#revoke_db_security_group_ingress)
        """

    def start_activity_stream(
        self, **kwargs: Unpack[StartActivityStreamRequestTypeDef]
    ) -> StartActivityStreamResponseTypeDef:
        """
        Starts a database activity stream to monitor activity on the database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/start_activity_stream.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#start_activity_stream)
        """

    def start_db_cluster(
        self, **kwargs: Unpack[StartDBClusterMessageTypeDef]
    ) -> StartDBClusterResultTypeDef:
        """
        Starts an Amazon Aurora DB cluster that was stopped using the Amazon Web
        Services console, the stop-db-cluster CLI command, or the
        <code>StopDBCluster</code> operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/start_db_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#start_db_cluster)
        """

    def start_db_instance(
        self, **kwargs: Unpack[StartDBInstanceMessageTypeDef]
    ) -> StartDBInstanceResultTypeDef:
        """
        Starts an Amazon RDS DB instance that was stopped using the Amazon Web Services
        console, the stop-db-instance CLI command, or the <code>StopDBInstance</code>
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/start_db_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#start_db_instance)
        """

    def start_db_instance_automated_backups_replication(
        self, **kwargs: Unpack[StartDBInstanceAutomatedBackupsReplicationMessageTypeDef]
    ) -> StartDBInstanceAutomatedBackupsReplicationResultTypeDef:
        """
        Enables replication of automated backups to a different Amazon Web Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/start_db_instance_automated_backups_replication.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#start_db_instance_automated_backups_replication)
        """

    def start_export_task(
        self, **kwargs: Unpack[StartExportTaskMessageTypeDef]
    ) -> ExportTaskResponseTypeDef:
        """
        Starts an export of DB snapshot or DB cluster data to Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/start_export_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#start_export_task)
        """

    def stop_activity_stream(
        self, **kwargs: Unpack[StopActivityStreamRequestTypeDef]
    ) -> StopActivityStreamResponseTypeDef:
        """
        Stops a database activity stream that was started using the Amazon Web Services
        console, the <code>start-activity-stream</code> CLI command, or the
        <code>StartActivityStream</code> operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/stop_activity_stream.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#stop_activity_stream)
        """

    def stop_db_cluster(
        self, **kwargs: Unpack[StopDBClusterMessageTypeDef]
    ) -> StopDBClusterResultTypeDef:
        """
        Stops an Amazon Aurora DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/stop_db_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#stop_db_cluster)
        """

    def stop_db_instance(
        self, **kwargs: Unpack[StopDBInstanceMessageTypeDef]
    ) -> StopDBInstanceResultTypeDef:
        """
        Stops an Amazon RDS DB instance temporarily.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/stop_db_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#stop_db_instance)
        """

    def stop_db_instance_automated_backups_replication(
        self, **kwargs: Unpack[StopDBInstanceAutomatedBackupsReplicationMessageTypeDef]
    ) -> StopDBInstanceAutomatedBackupsReplicationResultTypeDef:
        """
        Stops automated backup replication for a DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/stop_db_instance_automated_backups_replication.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#stop_db_instance_automated_backups_replication)
        """

    def switchover_blue_green_deployment(
        self, **kwargs: Unpack[SwitchoverBlueGreenDeploymentRequestTypeDef]
    ) -> SwitchoverBlueGreenDeploymentResponseTypeDef:
        """
        Switches over a blue/green deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/switchover_blue_green_deployment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#switchover_blue_green_deployment)
        """

    def switchover_global_cluster(
        self, **kwargs: Unpack[SwitchoverGlobalClusterMessageTypeDef]
    ) -> SwitchoverGlobalClusterResultTypeDef:
        """
        Switches over the specified secondary DB cluster to be the new primary DB
        cluster in the global database cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/switchover_global_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#switchover_global_cluster)
        """

    def switchover_read_replica(
        self, **kwargs: Unpack[SwitchoverReadReplicaMessageTypeDef]
    ) -> SwitchoverReadReplicaResultTypeDef:
        """
        Switches over an Oracle standby database in an Oracle Data Guard environment,
        making it the new primary database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/switchover_read_replica.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#switchover_read_replica)
        """

    def generate_db_auth_token(
        self, DBHostname: str, Port: int, DBUsername: str, Region: str | None = ...
    ) -> str:
        """
        Generates an auth token used to connect to a db with IAM credentials.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/generate_db_auth_token.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#generate_db_auth_token)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_blue_green_deployments"]
    ) -> DescribeBlueGreenDeploymentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_certificates"]
    ) -> DescribeCertificatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_cluster_automated_backups"]
    ) -> DescribeDBClusterAutomatedBackupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_cluster_backtracks"]
    ) -> DescribeDBClusterBacktracksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_cluster_endpoints"]
    ) -> DescribeDBClusterEndpointsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_cluster_parameter_groups"]
    ) -> DescribeDBClusterParameterGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_cluster_parameters"]
    ) -> DescribeDBClusterParametersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_cluster_snapshots"]
    ) -> DescribeDBClusterSnapshotsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_clusters"]
    ) -> DescribeDBClustersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_engine_versions"]
    ) -> DescribeDBEngineVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_instance_automated_backups"]
    ) -> DescribeDBInstanceAutomatedBackupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_instances"]
    ) -> DescribeDBInstancesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_log_files"]
    ) -> DescribeDBLogFilesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_parameter_groups"]
    ) -> DescribeDBParameterGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_parameters"]
    ) -> DescribeDBParametersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_proxies"]
    ) -> DescribeDBProxiesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_proxy_endpoints"]
    ) -> DescribeDBProxyEndpointsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_proxy_target_groups"]
    ) -> DescribeDBProxyTargetGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_proxy_targets"]
    ) -> DescribeDBProxyTargetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_recommendations"]
    ) -> DescribeDBRecommendationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_security_groups"]
    ) -> DescribeDBSecurityGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_snapshot_tenant_databases"]
    ) -> DescribeDBSnapshotTenantDatabasesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_snapshots"]
    ) -> DescribeDBSnapshotsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_db_subnet_groups"]
    ) -> DescribeDBSubnetGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_engine_default_cluster_parameters"]
    ) -> DescribeEngineDefaultClusterParametersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_engine_default_parameters"]
    ) -> DescribeEngineDefaultParametersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_event_subscriptions"]
    ) -> DescribeEventSubscriptionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_events"]
    ) -> DescribeEventsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_export_tasks"]
    ) -> DescribeExportTasksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_global_clusters"]
    ) -> DescribeGlobalClustersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_integrations"]
    ) -> DescribeIntegrationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_option_group_options"]
    ) -> DescribeOptionGroupOptionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_option_groups"]
    ) -> DescribeOptionGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_orderable_db_instance_options"]
    ) -> DescribeOrderableDBInstanceOptionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_pending_maintenance_actions"]
    ) -> DescribePendingMaintenanceActionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_reserved_db_instances_offerings"]
    ) -> DescribeReservedDBInstancesOfferingsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_reserved_db_instances"]
    ) -> DescribeReservedDBInstancesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_source_regions"]
    ) -> DescribeSourceRegionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_tenant_databases"]
    ) -> DescribeTenantDatabasesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["download_db_log_file_portion"]
    ) -> DownloadDBLogFilePortionPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["db_cluster_available"]
    ) -> DBClusterAvailableWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["db_cluster_deleted"]
    ) -> DBClusterDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["db_cluster_snapshot_available"]
    ) -> DBClusterSnapshotAvailableWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["db_cluster_snapshot_deleted"]
    ) -> DBClusterSnapshotDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["db_instance_available"]
    ) -> DBInstanceAvailableWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["db_instance_deleted"]
    ) -> DBInstanceDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["db_snapshot_available"]
    ) -> DBSnapshotAvailableWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["db_snapshot_completed"]
    ) -> DBSnapshotCompletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["db_snapshot_deleted"]
    ) -> DBSnapshotDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["tenant_database_available"]
    ) -> TenantDatabaseAvailableWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["tenant_database_deleted"]
    ) -> TenantDatabaseDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_waiter)
        """
