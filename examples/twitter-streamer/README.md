Twitter Streamer for CloudFoundry using Twython and Python-CFWorker Module
================================================================================

This is a sample application showing how to deploy a simple Twitter Streamer
to Cloud Foundry using the Twython (Twitter API) and CFWorker module


To Deploy on Cloud Foundry
================================================================================

Set your environment variables for your cooresponding Twitter API Keys, the streamer
reads these in at runtime.

You can set via Shell env before execution, or add code to the example like below:
```
os.environ['APP_KEY']='1dpfNZl3GIAfXqvz2lweknfo83nfwkf9'
os.environ['APP_SECRET']='RemGJSEFdlc3jUC1UFBrILrroPq33jd74hnfkg85hdlsotcS'
os.environ['OAUTH_TOKEN']='2927712042-arh06ofwadawd9hNYawdawd1IeeQEawd323gfgtQaZYy129dTG'
os.environ['OAUTH_TOKEN_SECRET']='mr0OAceywawdawdeDAfnaxawdawd3r6iVr1YJwdfsdf1qig9nz'
```

Add a custom port parameter to the cfworker if being deoployed locally, or leave
as is for CF deployment

```
cfworker.cfworker(port=<port>)
```

Choose what to track on twitter

```
stream.statuses.filter(track='bigdata')
```

Update the manifest.yml file name and host parameters for your app/env

Push to CF!

```
cf push
```

license
================================================================================

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

<http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

