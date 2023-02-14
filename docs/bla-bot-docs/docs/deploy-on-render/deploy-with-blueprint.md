---
sidebar_position: 2
---

# Deploy with Blueprint

If you have made any changes to the source code, commit those changes using `git add .` followed by `git commit -m "your-commit-message"` and then push those changes to your REMOTE branch on either GitHub or GitLab (This is a mandatory requirement).


If you have already pushed your changes (your data files) to the remote repository; now you can deploy your bot on Render in just a few clicks.
We have provided a render app [blueprint specification](https://render.com/docs/blueprint-spec) which makes the deployment process much easier. Just click on the button below and sign into your Render account.  

:::tip QUICK TIP

If `Missing Blueprint repository URL` error occurs, you can connect your GitHub or GitLab repository to Render by clicking on `Connect` button on the `Connect a repository` section.

:::

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)  

You will have to provide the necessary values for the environment variables at first (You can refer the following table for details about the environment variables), except for `RENDER_APP_URL`.
Make sure to update that later. You can find environment variables section in the `Environment` tab of your web service for updating that.
