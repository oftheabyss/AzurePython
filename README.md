# AzurePython
This repository contains samples for using the Azure SDK for Python in both Azure Commercial and Azure Government clouds.

## Why I Created This Repository
Hybrid and multi-cloud environments are a headache to build solutions in, especially when you're the one standing up core infrastructure in an enterprise-level environment. Things really *should* be done in a fully-automated and repeatable way that works for *each* environment.

AWS makes working with Boto3 such a breeze. Azure on the otherhand, not going to get into it but things seem to work well when you're using AzureCloud (Azure Commercial, Azure Public Cloud) because that's the default environment for most people. Getting things to work in AzureCloud _**and**_ AzureUSGovernment was a nightmare. Not a lot of documentation exists that shows examples or how to get the Azure SDK for Python to work with AzureUSGovernment specifically

## The Eureka Moment
I realized that `base_url` is an accepted kwarg for most Azure SDK classes through countless nights of reverse engineering their source code. Unfortunately, I was extremely tired and still couldn't get classes to work when using AzureUSGovernment.

The key piece that was missing from SDK class instantiation was the `credential_scopes` kwarg, which is the Azure Resource Manager endpoint URL, appended with `.default`.

* AzureCloud: `['https://management.azure.com/.default']`
* AzureUSGovernment: `['https://management.usgovcloudapi.net/.default']`

By appending `.default` to the `base_url` and passing it to the SDK classes during instantiation, things started working! I just wish I had figured this out *before* writing a bunch of custom classes that hit the Azure APIs directly. Oh well, hopefully the examples in this repository save you from the countless hours of frustration I went through in attempting to get the Azure SDK for Python to work for both AzureCloud and AzureUSGovernment.
