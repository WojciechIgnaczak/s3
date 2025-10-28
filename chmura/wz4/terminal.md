u334535@user-Precision-3460:~$ az upgrade
This command is in preview and under development. Reference and support levels: https://aka.ms/CLI_refstatus
You already have the latest azure-cli version: 2.78.0
Upgrade finished.
u334535@user-Precision-3460:~$ ls -la .zure
ls: nie ma dostępu do '.zure': Nie ma takiego pliku ani katalogu
u334535@user-Precision-3460:~$ ls -la .azure
razem 52
drwxrwxr-x  5 u334535 u334535 4096 paź 28 08:32 .
drwxrwxrwx 29 u334535 u334535 4096 paź 28 08:31 ..
-rw-rw-r--  1 u334535 u334535    5 paź 28 08:31 az.json
-rw-rw-r--  1 u334535 u334535    5 paź 28 08:31 az.sess
-rw-rw-r--  1 u334535 u334535   67 paź 28 08:31 az_survey.json
-rw-rw-r--  1 u334535 u334535   61 paź 28 08:31 azureProfile.json
-rw-rw-r--  1 u334535 u334535 5672 paź 28 08:32 commandIndex.json
drwxrwxr-x  2 u334535 u334535 4096 paź 28 08:32 commands
-rw-------  1 u334535 u334535   27 paź 28 08:31 config
drwxrwxr-x  2 u334535 u334535 4096 paź 28 08:31 logs
drwxrwxr-x  2 u334535 u334535 4096 paź 28 08:32 telemetry
-rw-rw-r--  1 u334535 u334535  211 paź 28 08:31 versionCheck.json
u334535@user-Precision-3460:~$ az login
A web browser has been opened at https://login.microsoftonline.com/organizations/oauth2/v2.0/authorize. Please continue the login in the web browser. If no web browser is available or if the web browser fails to open, use device code flow with `az login --use-device-code`.
Gtk-Message: 08:33:24.015: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.
[10083, Main Thread] WARNING: GTK+ module /snap/firefox/7084/gnome-platform/usr/lib/gtk-2.0/modules/libcanberra-gtk-module.so cannot be loaded.
GTK+ 2.x symbols detected. Using GTK+ 2.x and GTK+ 3 in the same process is not supported.: 'glib warning', file /build/firefox/parts/firefox/build/toolkit/xre/nsSigHandlers.cpp:201

(firefox_firefox:10083): Gtk-WARNING **: 08:33:24.083: GTK+ module /snap/firefox/7084/gnome-platform/usr/lib/gtk-2.0/modules/libcanberra-gtk-module.so cannot be loaded.
GTK+ 2.x symbols detected. Using GTK+ 2.x and GTK+ 3 in the same process is not supported.
Gtk-Message: 08:33:24.083: Failed to load module "canberra-gtk-module"
[10083, Main Thread] WARNING: GTK+ module /snap/firefox/7084/gnome-platform/usr/lib/gtk-2.0/modules/libcanberra-gtk-module.so cannot be loaded.
GTK+ 2.x symbols detected. Using GTK+ 2.x and GTK+ 3 in the same process is not supported.: 'glib warning', file /build/firefox/parts/firefox/build/toolkit/xre/nsSigHandlers.cpp:201

(firefox_firefox:10083): Gtk-WARNING **: 08:33:24.084: GTK+ module /snap/firefox/7084/gnome-platform/usr/lib/gtk-2.0/modules/libcanberra-gtk-module.so cannot be loaded.
GTK+ 2.x symbols detected. Using GTK+ 2.x and GTK+ 3 in the same process is not supported.
Gtk-Message: 08:33:24.084: Failed to load module "canberra-gtk-module"

Retrieving tenants and subscriptions for the selection...

[Tenant and subscription selection]

No     Subscription name    Subscription ID                       Tenant
-----  -------------------  ------------------------------------  -----------------------
[1] *  Azure for Students   2b54bb5b-dda3-4c5f-b1db-de0ea9f71751  Politechnika Warszawska

The default is marked with an *; the default tenant is 'Politechnika Warszawska' and subscription is 'Azure for Students' (2b54bb5b-dda3-4c5f-b1db-de0ea9f71751).

Select a subscription and tenant (Type a number or Enter for no changes): 1

Tenant: Politechnika Warszawska
Subscription: Azure for Students (2b54bb5b-dda3-4c5f-b1db-de0ea9f71751)

[Announcements]
With the new Azure CLI login experience, you can select the subscription you want to use more easily. Learn more about it and its configuration at https://go.microsoft.com/fwlink/?linkid=2271236

If you encounter any problem, please open an issue at https://aka.ms/azclibug

[Warning] The login output has been updated. Please be aware that it no longer displays the full list of available subscriptions by default.

u334535@user-Precision-3460:~$ cat .azure/azureProfile.json
{"installationId": "71a180fc-b3d8-11f0-a3c4-cc96e512101c", "subscriptions": [{"id": "2b54bb5b-dda3-4c5f-b1db-de0ea9f71751", "name": "Azure for Students", "state": "Enabled", "user": {"name": "01190427@pw.edu.pl", "type": "user"}, "isDefault": true, "tenantId": "3b50229c-cd78-4588-9bcf-97b7629e2f0f", "environmentName": "AzureCloud", "homeTenantId": "3b50229c-cd78-4588-9bcf-97b7629e2f0f", "tenantDefaultDomain": "pw.edu.pl", "tenantDisplayName": "Politechnika Warszawska", "managedByTenants": []}]}u334535@user-Precision-3460:~$ 
u334535@user-Precision-3460:~$ az account list
[
  {
    "cloudName": "AzureCloud",
    "homeTenantId": "3b50229c-cd78-4588-9bcf-97b7629e2f0f",
    "id": "2b54bb5b-dda3-4c5f-b1db-de0ea9f71751",
    "isDefault": true,
    "managedByTenants": [],
    "name": "Azure for Students",
    "state": "Enabled",
    "tenantDefaultDomain": "pw.edu.pl",
    "tenantDisplayName": "Politechnika Warszawska",
    "tenantId": "3b50229c-cd78-4588-9bcf-97b7629e2f0f",
    "user": {
      "name": "01190427@pw.edu.pl",
      "type": "user"
    }
  }
]
u334535@user-Precision-3460:~$ az account list --output table
Name                CloudName    SubscriptionId                        TenantId                              State    IsDefault
------------------  -----------  ------------------------------------  ------------------------------------  -------  -----------
Azure for Students  AzureCloud   2b54bb5b-dda3-4c5f-b1db-de0ea9f71751  3b50229c-cd78-4588-9bcf-97b7629e2f0f  Enabled  True
u334535@user-Precision-3460:~$ az ad
the following arguments are required: _subcommand

Examples from AI knowledge base:
az ad sp list --display-name mydisplay
List service principals. (autogenerated)

https://docs.microsoft.com/en-US/cli/azure/ad/sp#az_ad_sp_list
Read more about the command in reference docs
u334535@user-Precision-3460:~$ az ad sp list
^Cu334535@user-Precision-3460:~az ad sp create-for-rbac --name "MojServicePrincipal" --role "Contributor" --scopes "/subscriptions/2b54bb5b-dda3-4c5f-b1db-de0ea9f71751"1"
Directory permission is needed for the current user to register the application. For how to configure, please refer 'https://learn.microsoft.com/azure/azure-resource-manager/resource-group-create-service-principal-portal'. Original error: Insufficient privileges to complete the operation.
u334535@user-Precision-3460:~$ az vm
the following arguments are required: _subcommand

Examples from AI knowledge base:
az vm list
List all VMs.

az vm list-ip-addresses --resource-group MyResourceGroup --name MyVm
Get the IP addresses for a VM.

https://docs.microsoft.com/en-US/cli/azure/vm#az_vm_list
Read more about the command in reference docs
u334535@user-Precision-3460:~$ az vm list
[]
u334535@user-Precision-3460:~$ az group list
[]
u334535@user-Precision-3460:~$ az group create --name "CLI-Workshop-RG" --location "westeurope"
{
  "id": "/subscriptions/2b54bb5b-dda3-4c5f-b1db-de0ea9f71751/resourceGroups/CLI-Workshop-RG",
  "location": "westeurope",
  "managedBy": null,
  "name": "CLI-Workshop-RG",
  "properties": {
    "provisioningState": "Succeeded"
  },
  "tags": null,
  "type": "Microsoft.Resources/resourceGroups"
}
u334535@user-Precision-3460:~$ az group list
[
  {
    "id": "/subscriptions/2b54bb5b-dda3-4c5f-b1db-de0ea9f71751/resourceGroups/CLI-Workshop-RG",
    "location": "westeurope",
    "managedBy": null,
    "name": "CLI-Workshop-RG",
    "properties": {
      "provisioningState": "Succeeded"
    },
    "tags": null,
    "type": "Microsoft.Resources/resourceGroups"
  }
]
u334535@user-Precision-3460:~$ az group show --name "CLI-Workshop-RG"
{
  "id": "/subscriptions/2b54bb5b-dda3-4c5f-b1db-de0ea9f71751/resourceGroups/CLI-Workshop-RG",
  "location": "westeurope",
  "managedBy": null,
  "name": "CLI-Workshop-RG",
  "properties": {
    "provisioningState": "Succeeded"
  },
  "tags": null,
  "type": "Microsoft.Resources/resourceGroups"
}
u334535@user-Precision-3460:~$ az group list
[
  {
    "id": "/subscriptions/2b54bb5b-dda3-4c5f-b1db-de0ea9f71751/resourceGroups/CLI-Workshop-RG",
    "location": "westeurope",
    "managedBy": null,
    "name": "CLI-Workshop-RG",
    "properties": {
      "provisioningState": "Succeeded"
    },
    "tags": null,
    "type": "Microsoft.Resources/resourceGroups"
  }
]
u334535@user-Precision-3460:~$ az group delete --resource-group CLI-Workshop-RG
Are you sure you want to perform this operation? (y/n): y
u334535@user-Precision-3460:~$ az storage
the following arguments are required: _subcommand

Examples from AI knowledge base:
az storage account list
List all storage accounts in a subscription.

https://docs.microsoft.com/en-US/cli/azure/storage/account#az_storage_account_list
Read more about the command in reference docs
u334535@user-Precision-3460:~$ az group create --name "cli-tutorial" --location "polandcentral"
{
  "id": "/subscriptions/2b54bb5b-dda3-4c5f-b1db-de0ea9f71751/resourceGroups/cli-tutorial",
  "location": "polandcentral",
  "managedBy": null,
  "name": "cli-tutorial",
  "properties": {
    "provisioningState": "Succeeded"
  },
  "tags": null,
  "type": "Microsoft.Resources/resourceGroups"
}
u334535@user-Precision-3460:~$ az storage account create \
--name mojstorage334535 \
--resource-group cli-tutorial \
--location polandcentral \
--sku Standard_LRS \
--kind StorageV2
(SubscriptionNotFound) Subscription 2b54bb5b-dda3-4c5f-b1db-de0ea9f71751 was not found.
Code: SubscriptionNotFound
Message: Subscription 2b54bb5b-dda3-4c5f-b1db-de0ea9f71751 was not found.
u334535@user-Precision-3460:~$ az storage account create --name mojstorage334535 --resource-group cli-tutorial --location polandcentral --sku Standard_LRS --kind StorageV2
(SubscriptionNotFound) Subscription 2b54bb5b-dda3-4c5f-b1db-de0ea9f71751 was not found.
Code: SubscriptionNotFound
Message: Subscription 2b54bb5b-dda3-4c5f-b1db-de0ea9f71751 was not found.
u334535@user-Precision-3460:~$ az account list
[
  {
    "cloudName": "AzureCloud",
    "homeTenantId": "3b50229c-cd78-4588-9bcf-97b7629e2f0f",
    "id": "2b54bb5b-dda3-4c5f-b1db-de0ea9f71751",
    "isDefault": true,
    "managedByTenants": [],
    "name": "Azure for Students",
    "state": "Enabled",
    "tenantDefaultDomain": "pw.edu.pl",
    "tenantDisplayName": "Politechnika Warszawska",
    "tenantId": "3b50229c-cd78-4588-9bcf-97b7629e2f0f",
    "user": {
      "name": "01190427@pw.edu.pl",
      "type": "user"
    }
  }
]
u334535@user-Precision-3460:~$ az account list -o table
Name                CloudName    SubscriptionId                        TenantId                              State    IsDefault
------------------  -----------  ------------------------------------  ------------------------------------  -------  -----------
Azure for Students  AzureCloud   2b54bb5b-dda3-4c5f-b1db-de0ea9f71751  3b50229c-cd78-4588-9bcf-97b7629e2f0f  Enabled  True
u334535@user-Precision-3460:~$ az storage account create --name mojstorage334535 --resource-group cli-tutorial --location polandcentral --sku Standard_LRS --kind StorageV2
(SubscriptionNotFound) Subscription 2b54bb5b-dda3-4c5f-b1db-de0ea9f71751 was not found.
Code: SubscriptionNotFound
Message: Subscription 2b54bb5b-dda3-4c5f-b1db-de0ea9f71751 was not found.
u334535@user-Precision-3460:~$ az storage account create \
--name mojstorage334535 \
--resource-group cli-tutorial \
--location "polandcentral" \
--sku Standard_LRS \
--kind StorageV2
(SubscriptionNotFound) Subscription 2b54bb5b-dda3-4c5f-b1db-de0ea9f71751 was not found.
Code: SubscriptionNotFound
Message: Subscription 2b54bb5b-dda3-4c5f-b1db-de0ea9f71751 was not found.
u334535@user-Precision-3460:~$ az storage account create \
--name mojstorage334535 \
--resource-group cli-tutorial \
--location "polandcentral" \
--sku Standard_LRS \
--kind StorageV2
--subscription 2b54bb5b-dda3-4c5f-b1db-de0ea9f71751
(SubscriptionNotFound) Subscription 2b54bb5b-dda3-4c5f-b1db-de0ea9f71751 was not found.
Code: SubscriptionNotFound
Message: Subscription 2b54bb5b-dda3-4c5f-b1db-de0ea9f71751 was not found.
--subscription: nie znaleziono polecenia
u334535@user-Precision-3460:~$ az storage account create \
--name mojstorage334535 \
--resource-group cli-tutorial \
--location uksouth \
--sku Standard_LRS \
--kind StorageV2
(SubscriptionNotFound) Subscription 2b54bb5b-dda3-4c5f-b1db-de0ea9f71751 was not found.
Code: SubscriptionNotFound
Message: Subscription 2b54bb5b-dda3-4c5f-b1db-de0ea9f71751 was not found.
u334535@user-Precision-3460:~$ az account
the following arguments are required: _subcommand

Examples from AI knowledge base:
az account list
Get a list of subscriptions for the logged in account. (autogenerated)

az account show
Get the details of a subscription. (autogenerated)

az account set --subscription mysubscription
Set a subscription to be the current active subscription. (autogenerated)

https://docs.microsoft.com/en-US/cli/azure/account#az_account_list
Read more about the command in reference docs
u334535@user-Precision-3460:~$ az account list
[
  {
    "cloudName": "AzureCloud",
    "homeTenantId": "3b50229c-cd78-4588-9bcf-97b7629e2f0f",
    "id": "2b54bb5b-dda3-4c5f-b1db-de0ea9f71751",
    "isDefault": true,
    "managedByTenants": [],
    "name": "Azure for Students",
    "state": "Enabled",
    "tenantDefaultDomain": "pw.edu.pl",
    "tenantDisplayName": "Politechnika Warszawska",
    "tenantId": "3b50229c-cd78-4588-9bcf-97b7629e2f0f",
    "user": {
      "name": "01190427@pw.edu.pl",
      "type": "user"
    }
  }
]
u334535@user-Precision-3460:~$ az group list
[
  {
    "id": "/subscriptions/2b54bb5b-dda3-4c5f-b1db-de0ea9f71751/resourceGroups/cli-tutorial",
    "location": "polandcentral",
    "managedBy": null,
    "name": "cli-tutorial",
    "properties": {
      "provisioningState": "Succeeded"
    },
    "tags": null,
    "type": "Microsoft.Resources/resourceGroups"
  }
]
u334535@user-Precision-3460:~$ az login
A web browser has been opened at https://login.microsoftonline.com/organizations/oauth2/v2.0/authorize. Please continue the login in the web browser. If no web browser is available or if the web browser fails to open, use device code flow with `az login --use-device-code`.
Gtk-Message: 09:24:37.954: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.
[13154, Main Thread] WARNING: GTK+ module /snap/firefox/7084/gnome-platform/usr/lib/gtk-2.0/modules/libcanberra-gtk-module.so cannot be loaded.
GTK+ 2.x symbols detected. Using GTK+ 2.x and GTK+ 3 in the same process is not supported.: 'glib warning', file /build/firefox/parts/firefox/build/toolkit/xre/nsSigHandlers.cpp:201

(firefox_firefox:13154): Gtk-WARNING **: 09:24:38.060: GTK+ module /snap/firefox/7084/gnome-platform/usr/lib/gtk-2.0/modules/libcanberra-gtk-module.so cannot be loaded.
GTK+ 2.x symbols detected. Using GTK+ 2.x and GTK+ 3 in the same process is not supported.
Gtk-Message: 09:24:38.060: Failed to load module "canberra-gtk-module"
[13154, Main Thread] WARNING: GTK+ module /snap/firefox/7084/gnome-platform/usr/lib/gtk-2.0/modules/libcanberra-gtk-module.so cannot be loaded.
GTK+ 2.x symbols detected. Using GTK+ 2.x and GTK+ 3 in the same process is not supported.: 'glib warning', file /build/firefox/parts/firefox/build/toolkit/xre/nsSigHandlers.cpp:201

(firefox_firefox:13154): Gtk-WARNING **: 09:24:38.061: GTK+ module /snap/firefox/7084/gnome-platform/usr/lib/gtk-2.0/modules/libcanberra-gtk-module.so cannot be loaded.
GTK+ 2.x symbols detected. Using GTK+ 2.x and GTK+ 3 in the same process is not supported.
Gtk-Message: 09:24:38.061: Failed to load module "canberra-gtk-module"

Retrieving tenants and subscriptions for the selection...

[Tenant and subscription selection]

No     Subscription name    Subscription ID                       Tenant
-----  -------------------  ------------------------------------  -----------------------
[1] *  Azure for Students   2b54bb5b-dda3-4c5f-b1db-de0ea9f71751  Politechnika Warszawska

The default is marked with an *; the default tenant is 'Politechnika Warszawska' and subscription is 'Azure for Students' (2b54bb5b-dda3-4c5f-b1db-de0ea9f71751).

Select a subscription and tenant (Type a number or Enter for no changes): 1

Tenant: Politechnika Warszawska
Subscription: Azure for Students (2b54bb5b-dda3-4c5f-b1db-de0ea9f71751)

[Announcements]
With the new Azure CLI login experience, you can select the subscription you want to use more easily. Learn more about it and its configuration at https://go.microsoft.com/fwlink/?linkid=2271236

If you encounter any problem, please open an issue at https://aka.ms/azclibug

[Warning] The login output has been updated. Please be aware that it no longer displays the full list of available subscriptions by default.

u334535@user-Precision-3460:~$ az account list
[
  {
    "cloudName": "AzureCloud",
    "homeTenantId": "3b50229c-cd78-4588-9bcf-97b7629e2f0f",
    "id": "2b54bb5b-dda3-4c5f-b1db-de0ea9f71751",
    "isDefault": true,
    "managedByTenants": [],
    "name": "Azure for Students",
    "state": "Enabled",
    "tenantDefaultDomain": "pw.edu.pl",
    "tenantDisplayName": "Politechnika Warszawska",
    "tenantId": "3b50229c-cd78-4588-9bcf-97b7629e2f0f",
    "user": {
      "name": "01190427@pw.edu.pl",
      "type": "user"
    }
  }
]
u334535@user-Precision-3460:~$ az storage account create --name mojstorage334535 --resource-group cli-tutorial --location uksouth --sku Standard_LRS --kind StorageV2
(SubscriptionNotFound) Subscription 2b54bb5b-dda3-4c5f-b1db-de0ea9f71751 was not found.
Code: SubscriptionNotFound
Message: Subscription 2b54bb5b-dda3-4c5f-b1db-de0ea9f71751 was not found.
u334535@user-Precision-3460:~$ az group list
[
  {
    "id": "/subscriptions/2b54bb5b-dda3-4c5f-b1db-de0ea9f71751/resourceGroups/cli-tutorial",
    "location": "polandcentral",
    "managedBy": null,
    "name": "cli-tutorial",
    "properties": {
      "provisioningState": "Succeeded"
    },
    "tags": null,
    "type": "Microsoft.Resources/resourceGroups"
  }
]
u334535@user-Precision-3460:~$ az group
the following arguments are required: _subcommand

Examples from AI knowledge base:
az group create --location westus --resource-group MyResourceGroup
Create a new resource group in the West US region.

az group delete --resource-group MyResourceGroup
Delete a resource group.

az group list --query "[?location=='westus']"
List all resource groups located in the West US region.

https://docs.microsoft.com/en-US/cli/azure/group#az_group_list
Read more about the command in reference docs
u334535@user-Precision-3460:~$ az login --tenant 3b50229c-cd78-4588-9bcf-97b7629e2f0f
A web browser has been opened at https://login.microsoftonline.com/3b50229c-cd78-4588-9bcf-97b7629e2f0f/oauth2/v2.0/authorize. Please continue the login in the web browser. If no web browser is available or if the web browser fails to open, use device code flow with `az login --use-device-code`.
Gtk-Message: 09:31:10.632: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.
[14044, Main Thread] WARNING: GTK+ module /snap/firefox/7084/gnome-platform/usr/lib/gtk-2.0/modules/libcanberra-gtk-module.so cannot be loaded.
GTK+ 2.x symbols detected. Using GTK+ 2.x and GTK+ 3 in the same process is not supported.: 'glib warning', file /build/firefox/parts/firefox/build/toolkit/xre/nsSigHandlers.cpp:201

(firefox_firefox:14044): Gtk-WARNING **: 09:31:10.675: GTK+ module /snap/firefox/7084/gnome-platform/usr/lib/gtk-2.0/modules/libcanberra-gtk-module.so cannot be loaded.
GTK+ 2.x symbols detected. Using GTK+ 2.x and GTK+ 3 in the same process is not supported.
Gtk-Message: 09:31:10.675: Failed to load module "canberra-gtk-module"
[14044, Main Thread] WARNING: GTK+ module /snap/firefox/7084/gnome-platform/usr/lib/gtk-2.0/modules/libcanberra-gtk-module.so cannot be loaded.
GTK+ 2.x symbols detected. Using GTK+ 2.x and GTK+ 3 in the same process is not supported.: 'glib warning', file /build/firefox/parts/firefox/build/toolkit/xre/nsSigHandlers.cpp:201

(firefox_firefox:14044): Gtk-WARNING **: 09:31:10.676: GTK+ module /snap/firefox/7084/gnome-platform/usr/lib/gtk-2.0/modules/libcanberra-gtk-module.so cannot be loaded.
GTK+ 2.x symbols detected. Using GTK+ 2.x and GTK+ 3 in the same process is not supported.
Gtk-Message: 09:31:10.676: Failed to load module "canberra-gtk-module"

Retrieving subscriptions for the selection...

[Tenant and subscription selection]

No     Subscription name    Subscription ID                       Tenant
-----  -------------------  ------------------------------------  ------------------------------------
[1] *  Azure for Students   2b54bb5b-dda3-4c5f-b1db-de0ea9f71751  3b50229c-cd78-4588-9bcf-97b7629e2f0f

The default is marked with an *; the default tenant is '3b50229c-cd78-4588-9bcf-97b7629e2f0f' and subscription is 'Azure for Students' (2b54bb5b-dda3-4c5f-b1db-de0ea9f71751).

Select a subscription and tenant (Type a number or Enter for no changes): 1

Tenant: 3b50229c-cd78-4588-9bcf-97b7629e2f0f
Subscription: Azure for Students (2b54bb5b-dda3-4c5f-b1db-de0ea9f71751)

[Announcements]
With the new Azure CLI login experience, you can select the subscription you want to use more easily. Learn more about it and its configuration at https://go.microsoft.com/fwlink/?linkid=2271236

If you encounter any problem, please open an issue at https://aka.ms/azclibug

[Warning] The login output has been updated. Please be aware that it no longer displays the full list of available subscriptions by default.

u334535@user-Precision-3460:~$ az account list
[
  {
    "cloudName": "AzureCloud",
    "homeTenantId": "3b50229c-cd78-4588-9bcf-97b7629e2f0f",
    "id": "2b54bb5b-dda3-4c5f-b1db-de0ea9f71751",
    "isDefault": true,
    "managedByTenants": [],
    "name": "Azure for Students",
    "state": "Enabled",
    "tenantId": "3b50229c-cd78-4588-9bcf-97b7629e2f0f",
    "user": {
      "name": "01190427@pw.edu.pl",
      "type": "user"
    }
  }
]
u334535@user-Precision-3460:~$ az storage account create --name mojstorage334535 --resource-group cli-tutorial --location uksouth --sku Standard_LRS --kind StorageV2
(SubscriptionNotFound) Subscription 2b54bb5b-dda3-4c5f-b1db-de0ea9f71751 was not found.
Code: SubscriptionNotFound
Message: Subscription 2b54bb5b-dda3-4c5f-b1db-de0ea9f71751 was not found.
u334535@user-Precision-3460:~$ az storage account list
[]
u334535@user-Precision-3460:~$ az vm list
[]
u334535@user-Precision-3460:~$ az vm create
the following arguments are required: --name/-n, --resource-group/-g

Examples from AI knowledge base:
az vm create --name MyVm --resource-group MyResourceGroup --image RedHat:RHEL:7-RAW:7.4.2018010506
Create a default RedHat VM with automatic SSH authentication using an image URN.

az vm create --name MyVm --resource-group rg1 --image debian --assign-identity /subscriptions/99999999-1bf0-4dda-aec3-cb9272f09590/resourcegroups/myRG/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myID
Create a debian VM with a user assigned identity.

az group create --location westus --resource-group MyResourceGroup
Create a new resource group in the West US region.

https://docs.microsoft.com/en-US/cli/azure/vm#az_vm_create
Read more about the command in reference docs
u334535@user-Precision-3460:~$ az vm create --resource-group cli-tutorial --name myVMPW --image Ubuntu2404 --size Standard_B1s --admin-username azureuser --generate-ssh-keys --no-wait --location uksouth
The default value of '--size' will be changed to 'Standard_D2s_v5' from 'Standard_DS1_v2' in a future release.
SSH key files '/home/u334535/.ssh/id_rsa' and '/home/u334535/.ssh/id_rsa.pub' have been generated under ~/.ssh to allow SSH access to the VM. If using machines without permanent storage, back up your keys to a safe location.
The command failed with an unexpected error. Here is the traceback:
The content for this response was already consumed
Traceback (most recent call last):
  File "/opt/az/lib/python3.13/site-packages/azure/cli/core/commands/__init__.py", line 703, in _run_job
    result = cmd_copy(params)
  File "/opt/az/lib/python3.13/site-packages/azure/cli/core/commands/__init__.py", line 336, in __call__
    return self.handler(*args, **kwargs)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/opt/az/lib/python3.13/site-packages/azure/cli/core/commands/command_operation.py", line 120, in handler
    return op(**command_args)
  File "/opt/az/lib/python3.13/site-packages/azure/cli/command_modules/vm/custom.py", line 1193, in create_vm
    return sdk_no_wait(no_wait, client.begin_create_or_update, resource_group_name, deployment_name, deployment)
  File "/opt/az/lib/python3.13/site-packages/azure/cli/core/util.py", line 759, in sdk_no_wait
    return func(*args, **kwargs)
  File "/opt/az/lib/python3.13/site-packages/azure/core/tracing/decorator.py", line 119, in wrapper_use_tracer
    return func(*args, **kwargs)
  File "/opt/az/lib/python3.13/site-packages/azure/mgmt/resource/resources/v2024_11_01/operations/_operations.py", line 7094, in begin_create_or_update
    raw_result = self._create_or_update_initial(
        resource_group_name=resource_group_name,
    ...<7 lines>...
        **kwargs
    )
  File "/opt/az/lib/python3.13/site-packages/azure/mgmt/resource/resources/v2024_11_01/operations/_operations.py", line 6987, in _create_or_update_initial
    raise HttpResponseError(response=response, error_format=ARMErrorFormat)
azure.core.exceptions.HttpResponseError: (InvalidTemplateDeployment) The template deployment failed with multiple errors. Please see details for more information.
Code: InvalidTemplateDeployment
Message: The template deployment failed with multiple errors. Please see details for more information.
Exception Details:	(RequestDisallowedByAzure) Resource 'myVMPWVNET' was disallowed by Azure: This policy maintains a set of best available regions where your subscription can deploy resources. The objective of this policy is to ensure that your subscription has full access to Azure services with optimal performance. Should you need additional or different regions, contact support..
	Code: RequestDisallowedByAzure
	Message: Resource 'myVMPWVNET' was disallowed by Azure: This policy maintains a set of best available regions where your subscription can deploy resources. The objective of this policy is to ensure that your subscription has full access to Azure services with optimal performance. Should you need additional or different regions, contact support..
	Target: myVMPWVNET	(RequestDisallowedByAzure) Resource 'myVMPWNSG' was disallowed by Azure: This policy maintains a set of best available regions where your subscription can deploy resources. The objective of this policy is to ensure that your subscription has full access to Azure services with optimal performance. Should you need additional or different regions, contact support..
	Code: RequestDisallowedByAzure
	Message: Resource 'myVMPWNSG' was disallowed by Azure: This policy maintains a set of best available regions where your subscription can deploy resources. The objective of this policy is to ensure that your subscription has full access to Azure services with optimal performance. Should you need additional or different regions, contact support..
	Target: myVMPWNSG	(RequestDisallowedByAzure) Resource 'myVMPWPublicIP' was disallowed by Azure: This policy maintains a set of best available regions where your subscription can deploy resources. The objective of this policy is to ensure that your subscription has full access to Azure services with optimal performance. Should you need additional or different regions, contact support..
	Code: RequestDisallowedByAzure
	Message: Resource 'myVMPWPublicIP' was disallowed by Azure: This policy maintains a set of best available regions where your subscription can deploy resources. The objective of this policy is to ensure that your subscription has full access to Azure services with optimal performance. Should you need additional or different regions, contact support..
	Target: myVMPWPublicIP	(RequestDisallowedByAzure) Resource 'myVMPWVMNic' was disallowed by Azure: This policy maintains a set of best available regions where your subscription can deploy resources. The objective of this policy is to ensure that your subscription has full access to Azure services with optimal performance. Should you need additional or different regions, contact support..
	Code: RequestDisallowedByAzure
	Message: Resource 'myVMPWVMNic' was disallowed by Azure: This policy maintains a set of best available regions where your subscription can deploy resources. The objective of this policy is to ensure that your subscription has full access to Azure services with optimal performance. Should you need additional or different regions, contact support..
	Target: myVMPWVMNic	(RequestDisallowedByAzure) Resource 'myVMPW' was disallowed by Azure: This policy maintains a set of best available regions where your subscription can deploy resources. The objective of this policy is to ensure that your subscription has full access to Azure services with optimal performance. Should you need additional or different regions, contact support..
	Code: RequestDisallowedByAzure
	Message: Resource 'myVMPW' was disallowed by Azure: This policy maintains a set of best available regions where your subscription can deploy resources. The objective of this policy is to ensure that your subscription has full access to Azure services with optimal performance. Should you need additional or different regions, contact support..
	Target: myVMPW

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/opt/az/lib/python3.13/site-packages/azure/cli/core/commands/arm.py", line 109, in handle_template_based_exception
    raise CLIError(ex.inner_exception.error.message)
                   ^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'error'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/opt/az/lib/python3.13/site-packages/knack/cli.py", line 233, in invoke
    cmd_result = self.invocation.execute(args)
  File "/opt/az/lib/python3.13/site-packages/azure/cli/core/commands/__init__.py", line 666, in execute
    raise ex
  File "/opt/az/lib/python3.13/site-packages/azure/cli/core/commands/__init__.py", line 734, in _run_jobs_serially
    results.append(self._run_job(expanded_arg, cmd_copy))
                   ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/az/lib/python3.13/site-packages/azure/cli/core/commands/__init__.py", line 726, in _run_job
    return cmd_copy.exception_handler(ex)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^
  File "/opt/az/lib/python3.13/site-packages/azure/cli/core/commands/arm.py", line 112, in handle_template_based_exception
    raise_subdivision_deployment_error(ex.response.internal_response.text, ex.error.code if ex.error else None)
                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/az/lib/python3.13/site-packages/requests/models.py", line 926, in text
    if not self.content:
           ^^^^^^^^^^^^
  File "/opt/az/lib/python3.13/site-packages/requests/models.py", line 897, in content
    raise RuntimeError("The content for this response was already consumed")
RuntimeError: The content for this response was already consumed
To check existing issues, please visit: https://github.com/Azure/azure-cli/issues
u334535@user-Precision-3460:~$ az vm create --resource-group cli-tutorial --name myVMPW --image Ubuntu2404 --size Standard_B1s --admin-username azureuser --generate-ssh-keys --no-wait --location polandcentral
The default value of '--size' will be changed to 'Standard_D2s_v5' from 'Standard_DS1_v2' in a future release.
u334535@user-Precision-3460:~$ az vm show -d --resource-group cli-tutorial --name myVMPW --query publicIps
(ResourceNotFound) The Resource 'Microsoft.Compute/virtualMachines/myVMPW' under resource group 'cli-tutorial' was not found. For more details please go to https://aka.ms/ARMResourceNotFoundFix
Code: ResourceNotFound
Message: The Resource 'Microsoft.Compute/virtualMachines/myVMPW' under resource group 'cli-tutorial' was not found. For more details please go to https://aka.ms/ARMResourceNotFoundFix
u334535@user-Precision-3460:~$ az group show
the following arguments are required: --name/-n/--resource-group/-g

Examples from AI knowledge base:
az group show --resource-group myresourcegroup
Gets a resource group. (autogenerated)

az account show
Get the details of a subscription. (autogenerated)

az group list --query "[?location=='westus']"
List all resource groups located in the West US region.

https://docs.microsoft.com/en-US/cli/azure/group#az_group_show
Read more about the command in reference docs
u334535@user-Precision-3460:~$ az group list
[
  {
    "id": "/subscriptions/2b54bb5b-dda3-4c5f-b1db-de0ea9f71751/resourceGroups/cli-tutorial",
    "location": "polandcentral",
    "managedBy": null,
    "name": "cli-tutorial",
    "properties": {
      "provisioningState": "Succeeded"
    },
    "tags": null,
    "type": "Microsoft.Resources/resourceGroups"
  },
  {
    "id": "/subscriptions/2b54bb5b-dda3-4c5f-b1db-de0ea9f71751/resourceGroups/NetworkWatcherRG",
    "location": "polandcentral",
    "managedBy": null,
    "name": "NetworkWatcherRG",
    "properties": {
      "provisioningState": "Succeeded"
    },
    "tags": null,
    "type": "Microsoft.Resources/resourceGroups"
  }
]
u334535@user-Precision-3460:~$ az vm list
[]
u334535@user-Precision-3460:~$ az vm stop
(--resource-group --name | --ids) are required
u334535@user-Precision-3460:~$ az vm stop --resource-name cli-tutorial --name myVMPW
unrecognized arguments: --resource-name cli-tutorial

Examples from AI knowledge base:
az vm stop --resource-group MyResourceGroup --name MyVm
Power off (stop) a running VM.

az vm stop --resource-group MyResourceGroup --name MyVm --skip-shutdown
Power off a running VM without shutting down.

https://docs.microsoft.com/en-US/cli/azure/vm#az_vm_stop
Read more about the command in reference docs
u334535@user-Precision-3460:~$ az vm list
[]
u334535@user-Precision-3460:~$ az vm create --resource-group cli-tutorial --name myVMPW --image Ubuntu2404 --size Standard_B1s --admin-username azureuser --generate-ssh-keys --location polandcentral
The default value of '--size' will be changed to 'Standard_D2s_v5' from 'Standard_DS1_v2' in a future release.
{
  "fqdns": "",
  "id": "/subscriptions/2b54bb5b-dda3-4c5f-b1db-de0ea9f71751/resourceGroups/cli-tutorial/providers/Microsoft.Compute/virtualMachines/myVMPW",
  "location": "polandcentral",
  "macAddress": "7C-ED-8D-8B-A3-44",
  "powerState": "VM running",
  "privateIpAddress": "10.0.0.4",
  "publicIpAddress": "74.248.132.62",
  "resourceGroup": "cli-tutorial"
}
u334535@user-Precision-3460:~$ az vm list
[
  {
    "etag": "\"1\"",
    "hardwareProfile": {
      "vmSize": "Standard_B1s"
    },
    "id": "/subscriptions/2b54bb5b-dda3-4c5f-b1db-de0ea9f71751/resourceGroups/CLI-TUTORIAL/providers/Microsoft.Compute/virtualMachines/myVMPW",
    "location": "polandcentral",
    "name": "myVMPW",
    "networkProfile": {
      "networkInterfaces": [
        {
          "id": "/subscriptions/2b54bb5b-dda3-4c5f-b1db-de0ea9f71751/resourceGroups/cli-tutorial/providers/Microsoft.Network/networkInterfaces/myVMPWVMNic",
          "resourceGroup": "cli-tutorial"
        }
      ]
    },
    "osProfile": {
      "adminUsername": "azureuser",
      "allowExtensionOperations": true,
      "computerName": "myVMPW",
      "linuxConfiguration": {
        "disablePasswordAuthentication": true,
        "patchSettings": {
          "assessmentMode": "ImageDefault",
          "patchMode": "ImageDefault"
        },
        "provisionVMAgent": true,
        "ssh": {
          "publicKeys": [
            {
              "keyData": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCkitySGKCELkIOP87SLSRZo8ZEeGR2bFVoLbHAiQLb8JZ8wMlF/0Ias/dQbOlcC9L/XgpnS2W3mqeEXFSL88TFhFa8b6BDJu9J6hMA2zkiEdch+0SlOPcbArhMfeCwzLcT5hJv7EdPMG3UDRHnrJ8pJZkKQJAmSfkAHxyWbqql1XZK5lbRIm52afe8VPVylMNU+/l5Hpj1m2eiAok2dLoSFQPqtUfjfeXaYUP+HkY/CddNTSV1uCPIR5jotf3x11r+1KpoQMcbFBs97jVZBUcTYJzGoMs1AETMJPPpz87Z8j2936TU/B80t+ofja7SnrwpxvDgyNehenzpLlOAoYJ9",
              "path": "/home/azureuser/.ssh/authorized_keys"
            }
          ]
        }
      },
      "requireGuestProvisionSignal": true,
      "secrets": []
    },
    "provisioningState": "Succeeded",
    "resourceGroup": "CLI-TUTORIAL",
    "securityProfile": {
      "securityType": "TrustedLaunch",
      "uefiSettings": {
        "secureBootEnabled": true,
        "vTpmEnabled": true
      }
    },
    "storageProfile": {
      "dataDisks": [],
      "diskControllerType": "SCSI",
      "imageReference": {
        "exactVersion": "24.04.202510010",
        "offer": "ubuntu-24_04-lts",
        "publisher": "Canonical",
        "sku": "server",
        "version": "latest"
      },
      "osDisk": {
        "caching": "ReadWrite",
        "createOption": "FromImage",
        "deleteOption": "Detach",
        "diskSizeGB": 30,
        "managedDisk": {
          "id": "/subscriptions/2b54bb5b-dda3-4c5f-b1db-de0ea9f71751/resourceGroups/cli-tutorial/providers/Microsoft.Compute/disks/myVMPW_OsDisk_1_2fae3a6aebcb41d9ba11903cfa6c121c",
          "resourceGroup": "cli-tutorial",
          "storageAccountType": "Premium_LRS"
        },
        "name": "myVMPW_OsDisk_1_2fae3a6aebcb41d9ba11903cfa6c121c",
        "osType": "Linux"
      }
    },
    "tags": {},
    "timeCreated": "2025-10-28T09:04:20.6328797+00:00",
    "type": "Microsoft.Compute/virtualMachines",
    "vmId": "ca158054-a470-47b0-939c-ffbcda849894"
  }
]
u334535@user-Precision-3460:~$ az vm list --query "[?resourceGroup=='cli-tutorial'].{Name:name, Location:location, Size:hardwareProfile.vmSize}" --output table

u334535@user-Precision-3460:~$ az vm list -o table
Name    ResourceGroup    Location
------  ---------------  -------------
myVMPW  CLI-TUTORIAL     polandcentral
u334535@user-Precision-3460:~$ az vm list --query "[?resourceGroup=='CLI-TUTORIAL'].{Name:name, Location:location, Size:hardwareProfile.vmSize}" --output table
Name    Location       Size
------  -------------  ------------
myVMPW  polandcentral  Standard_B1s
u334535@user-Precision-3460:~$ az vm list
[
  {
    "etag": "\"1\"",
    "hardwareProfile": {
      "vmSize": "Standard_B1s"
    },
    "id": "/subscriptions/2b54bb5b-dda3-4c5f-b1db-de0ea9f71751/resourceGroups/CLI-TUTORIAL/providers/Microsoft.Compute/virtualMachines/myVMPW",
    "location": "polandcentral",
    "name": "myVMPW",
    "networkProfile": {
      "networkInterfaces": [
        {
          "id": "/subscriptions/2b54bb5b-dda3-4c5f-b1db-de0ea9f71751/resourceGroups/cli-tutorial/providers/Microsoft.Network/networkInterfaces/myVMPWVMNic",
          "resourceGroup": "cli-tutorial"
        }
      ]
    },
    "osProfile": {
      "adminUsername": "azureuser",
      "allowExtensionOperations": true,
      "computerName": "myVMPW",
      "linuxConfiguration": {
        "disablePasswordAuthentication": true,
        "patchSettings": {
          "assessmentMode": "ImageDefault",
          "patchMode": "ImageDefault"
        },
        "provisionVMAgent": true,
        "ssh": {
          "publicKeys": [
            {
              "keyData": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCkitySGKCELkIOP87SLSRZo8ZEeGR2bFVoLbHAiQLb8JZ8wMlF/0Ias/dQbOlcC9L/XgpnS2W3mqeEXFSL88TFhFa8b6BDJu9J6hMA2zkiEdch+0SlOPcbArhMfeCwzLcT5hJv7EdPMG3UDRHnrJ8pJZkKQJAmSfkAHxyWbqql1XZK5lbRIm52afe8VPVylMNU+/l5Hpj1m2eiAok2dLoSFQPqtUfjfeXaYUP+HkY/CddNTSV1uCPIR5jotf3x11r+1KpoQMcbFBs97jVZBUcTYJzGoMs1AETMJPPpz87Z8j2936TU/B80t+ofja7SnrwpxvDgyNehenzpLlOAoYJ9",
              "path": "/home/azureuser/.ssh/authorized_keys"
            }
          ]
        }
      },
      "requireGuestProvisionSignal": true,
      "secrets": []
    },
    "provisioningState": "Succeeded",
    "resourceGroup": "CLI-TUTORIAL",
    "securityProfile": {
      "securityType": "TrustedLaunch",
      "uefiSettings": {
        "secureBootEnabled": true,
        "vTpmEnabled": true
      }
    },
    "storageProfile": {
      "dataDisks": [],
      "diskControllerType": "SCSI",
      "imageReference": {
        "exactVersion": "24.04.202510010",
        "offer": "ubuntu-24_04-lts",
        "publisher": "Canonical",
        "sku": "server",
        "version": "latest"
      },
      "osDisk": {
        "caching": "ReadWrite",
        "createOption": "FromImage",
        "deleteOption": "Detach",
        "diskSizeGB": 30,
        "managedDisk": {
          "id": "/subscriptions/2b54bb5b-dda3-4c5f-b1db-de0ea9f71751/resourceGroups/cli-tutorial/providers/Microsoft.Compute/disks/myVMPW_OsDisk_1_2fae3a6aebcb41d9ba11903cfa6c121c",
          "resourceGroup": "cli-tutorial",
          "storageAccountType": "Premium_LRS"
        },
        "name": "myVMPW_OsDisk_1_2fae3a6aebcb41d9ba11903cfa6c121c",
        "osType": "Linux"
      }
    },
    "tags": {},
    "timeCreated": "2025-10-28T09:04:20.6328797+00:00",
    "type": "Microsoft.Compute/virtualMachines",
    "vmId": "ca158054-a470-47b0-939c-ffbcda849894"
  }
]
u334535@user-Precision-3460:~$ az vm list --query "[?resourceGroup=='CLI-TUTORIAL'].{Name:name, Location:location, Size:hardwareProfile.vmSize}" --output table
Name    Location       Size
------  -------------  ------------
myVMPW  polandcentral  Standard_B1s
u334535@user-Precision-3460:~$ az vm show
(--resource-group --name | --ids) are required
u334535@user-Precision-3460:~$ az vm show -d --resource-group cli-tutorial --name myVMPW --query publicIps
"74.248.132.62"
u334535@user-Precision-3460:~$ az vm show -d --resource-group cli-tutorial --name myVMPW --query publicIps --output tsv
74.248.132.62
u334535@user-Precision-3460:~$ VM_IP=$(az vm show -d --resource-group cli-tutorial --name myVMPW --query publicIps --output tsv)
u334535@user-Precision-3460:~$ echo $VM_IP
74.248.132.62
u334535@user-Precision-3460:~$ az group delete --ids /subscriptions/2b54bb5b-dda3-4c5f-b1db-de0ea9f71751/resourceGroups/cli-tutorial/providers/Microsoft.Compute/virtualMachines/myVMPW
the following arguments are required: --name/-n/--resource-group/-g

Examples from AI knowledge base:
az group delete --resource-group MyResourceGroup
Delete a resource group.

az group list --query "[?location=='westus']"
List all resource groups located in the West US region.

https://docs.microsoft.com/en-US/cli/azure/group#az_group_delete
Read more about the command in reference docs
u334535@user-Precision-3460:~$ az group delete --name "cli-tutorial"
Are you sure you want to perform this operation? (y/n): y
u334535@user-Precision-3460:~$ az vm list
[]
u334535@user-Precision-3460:~$ az logout
u334535@user-Precision-3460:~$ az group delete --name "cli-tutorial"

