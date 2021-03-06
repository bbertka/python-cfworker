Python-CFWorker: A Module to simplify Worker App deployment
================================================================================

This module makes it easier to deploy Python workers by wrapping Flask and multiprocessing
functionality into a single module. When instanced, your app will be serving http
via Flask, as well as performing work. 

https://pypi.python.org/pypi/python-cfworker

Recent Changes
================================================================================
1.7.0 - Fixed tab and spaces inconsistency for later versions of python

1.6.0 - Now using CF Diego 'PORT' environment for HTTP port binding

1.5.0 - Fixed simple worker to use CF port

1.4.1 - Removed auto-start from main class

1.4.0 - New implementation via multiprocessing.Process (added start, stop)

1.3.1 - Added new CF worker example for streaming twitter data


To Use
================================================================================

To get the latest version with new features, checkout the repository and run the setup script

```
sudo python setup.py install
```

To install a tested production version via pip:

```
pip install python-cfworker
```

To use within a CF app, check the examples folder

<pre>

import cfworker

if __name__=='__main__':

	worker = cfworker.cfworker()

	worker.start()

	while True:
		print 'working...'

	worker.stop()

</pre>


Note that by default the cfworker will run on Flask port 5000 unless otherwise specified:

```
cfworker.cfworker(port=<port>)
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

