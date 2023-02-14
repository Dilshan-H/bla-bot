---
sidebar_position: 3
---

# Deploy Manually

1. Login to your [Render account](https://dashboard.render.com/).
2. Click on `New Service` and select **web service**.
3. Now you can connect your GitHub or GitLab repository to Render.

After this process, you have to configure the environment variables as mentioned above. You can find environment variables section in the `Environment` tab of your web service.

Add these keys and respective values to the environment variables:

| Key            | Value                                                                                                                                                                    |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| DEV_CHAT_ID    | Your chat id obtained from _idbot_                                                                                                                                       |
| ENV            | `prod`                                                                                                                                                                   |
| GROUP_CHAT_ID  | Your group chat id obtained from _idbot_                                                                                                                                 |
| RENDER_APP_URL | The url of the Render app. (Ex: `https://your-bot-name.onrender.com`) - Can obtain from [Render Dashboard]([https://dashboard.render.com/](https://dashboard.render.com/)) |
| PORT           | `8443`                                                                                                                                                                   |
| SECRET_KEY     | Your secret key here obtained after data encryption procedure                                                                                                            |
| TELEGRAM_TOKEN | Your Telegram token obtained from _botfather_ earlier                                                                                                                 

  Now click on `Save Changes` and your bot will be deployed on Render.  