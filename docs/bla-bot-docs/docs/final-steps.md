---
sidebar_label: 'Final Steps'
sidebar_position: 8
---

# Final Steps

Now open your web browser and visit the following URL (You can also use Postman) - Make sure to replace the string `{YOUR-BOT-TOKEN}` with your bot's token and the `{RENDER-URL}` with your web service URL.  

https://api.telegram.org/bot{YOUR-BOT-TOKEN}/setWebhook?url={RENDER-URL}

You will get a response like this:

```json
{
  "ok": true,
  "result": true,
  "description": "Webhook was set"
}
```
:::tip QUICK TIP

You can verify webhook information using following URL:  
https://api.telegram.org/bot{YOUR-BOT-TOKEN}/getWebhookInfo

:::

If everything goes well, you can start using your bot right away. Open the Telegram app and search for your bot and start a conversation with it. Send `/help` to your bot to see the list of commands. Test all other features and make sure everything is working as expected.

Then add your bot to your group and start using it.

:::tip QUICK TIP

You can use [BotFather](https://t.me/botfather) to change the bot's name and profile picture. Also do not forget to add all the commands to your bot using BotFather (Edit Commands). So, users can easily browse all the commands.

:::