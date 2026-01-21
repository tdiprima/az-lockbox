# Setting Up Your `.env` File for Azure AI Foundry

Here's where you can find each value in Azure AI Foundry, the portal, or other relevant locations.

### GitHub
- `GITHUB_TOKEN` - Create a personal access token in GitHub, then paste it into the `GITHUB_TOKEN=` field in your `.env` file.

### Overview Page (Project)
- `AZURE_SUBSCRIPTION_ID` - Check **Project details** on the **Overview** page of your project.
- `AZURE_AI_PROJECT_NAME` - Look at the top of the **Overview** page for your project.
- `AZURE_OPENAI_SERVICE` - Find this in the **Included capabilities** tab for **Azure OpenAI Service** on the **Overview** page.
- `PROJECT_CONNECTION_STRING` - On the **Overview** page, go to **Project details** connection and copy the **Project connection string**.

### Management Center
- `AZURE_OPENAI_RESOURCE_GROUP` - Go to **Project properties** on the **Overview** page of the **Management Center**.
- `GLOBAL_LLM_SERVICE` - Under **Connected resources**, find the **Azure AI Services** connection name. If not listed, check the **Azure portal** under your resource group for the AI Services resource name.
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Under **Connected resources**, find the **Azure AI Search** connection and copy the **Endpoint** URL. You can also check the **Azure portal** under your **Azure AI Search** resource's **Overview**.

### Models + Endpoints Page
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Select your embedding model (e.g., `text-embedding-ada-002`) and note the **Deployment name** from the model details.
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Select your chat model (e.g., `gpt-4o-mini`) and note the **Deployment name** from the model details.

### Azure Portal
- `AZURE_OPENAI_ENDPOINT` - Look for **Azure AI services**, click on it, then go to **Resource Management**, **Keys and Endpoint**, scroll down to the "Azure OpenAI endpoints", and copy the one that says "Language APIs".
- `AZURE_OPENAI_API_KEY` - From the same screen, copy KEY 1 or KEY 2. 
- `AZURE_SEARCH_API_KEY` - Go to your **Azure AI Search** resource, then go to **Settings** and then **Keys** to copy the primary or secondary admin key.

### External Webpage
- `AZURE_OPENAI_API_VERSION` - Visit the [API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) page under **Latest GA API release**.
