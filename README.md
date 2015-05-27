Python-CFWorker: A Module to simplify Worker App deployment
================================================================================

This module makes it easier to deploy Python workers by wrapping Flask and Threading
functionality into a single module. When instanced, your app will be serving http
via Flask, as well as performing work. 

https://pypi.python.org/pypi/python-cfworker

To Use
================================================================================

To get the latest version, checkout the repository and run the setup script

```
sudo python setup.py install
```

To install via pip:

```
pip install python-cfworker
```

To use within a CF app, check the examples folder

Basically, the cfworker.run() function must be overridden with your app's
work.

<pre>

import cfworker


class cfworker(cfworker.cfworker):

        def run(self):
                # override with your functionality
                while True:
                        print "cfworker: Working..."


if __name__=='__main__':

        w = cfworker()

</pre>


Note that by default the cfworker will run on CF App port set by the environment:

```
VCAP_APP_PORT
```

If you would like to run locally, just add the port parameter to the cfworker() 
instance like so:

```
w = cfworker(port=8080)
```

If you would like different logging, import the logging module and set the log:

<pre>
import logging

...

w = cfworker(log=logging.ERROR)
</pre>


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

