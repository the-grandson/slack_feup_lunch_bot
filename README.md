# Slack - Almoços FEUP App
A very simple Slack app to respond with FEUP lunch menu.

## Instalation
When first developping this app I followed [Shaked Askayo tutorial](https://www.kubiya.ai/resource-post/how-to-build-a-slackbot-with-python).

### Slack App create and configure
1. Create a [Slack App](https://api.slack.com/apps).
2. Fill the App **Display Information**.
3. Activate the App **Socket Mode**.
4. Go to *App Home* and edit your bot **Diplay Name** and **Default Name**.
   - This step will generate your App [**Bot Token**](https://api.slack.com/authentication/token-types#bot) automatically.
5. Go to *OAuth and Permissions*, navigate to **Scopes->Bot Token Scopes** and add the following OAuth Scopes: **app_mentions:read** **chat:write**.
   - Once here, copy your **Bot User OAuth Token** to the **.env** file.
6. Go to *Event Subscriptions* and activate the toggle button in **Enable Events**.
   - Once here, expand **Subscribe to bot events** and add the bot user event **app_mention**.
7. Go to *Install App* and click the **Install** or **Reinstall to Workspace** button.
   - When installing the app you will be asked to select the Slack workspace.
8. Go to *Basic Information* and under **App-Level Tokens** click your **connections:write** token name to copy your **Slack App Token** to the **.env** file.

### Python script install (windows)
1. Considering you have *Python 3.10* and *pip* installed, open a command line and navigate to the *.venv* folder.
2. **Optional**, if you want to setup a contained dependency environment run `.\venv\Scripts\activate`.
3. Run `pip install -r requirements.txt` to install all the dependencies.
4. Run *python app.py* nd your application shoud be set-up.
5. **Optinal**, to make your script run on boot, execute *python autorun.py*.

## Usage
1. Add your bot to a channel in your workspace.
2. Mention your bot using `@botname` and it will answer with the current day lunch menus.
3. **Optional**, set a daily reminder to mention your bot daily using `/remind @botname to What is the lunch menu today? at 10:00 every weekday`
