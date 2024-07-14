# Cloud Computing : CI/CD Workflows [REST API Update]

The general structure of this repo is taken from the prior assignment, although I have a feeling that this isn't traditional structure, and I'm somewhat questioning whether I set this up correctly as per the assignment requests.
This repository currently contains code files for an extremely simple REST API, related tests, and Dockerfiles for both code files.

I'm going to be 100% honest here - I did not run this prior to committing - I just checked the code as best as I could and prepared to upload it.

## About the Workflow
The workflow in this repository should be configured to automatically run the test.py files in the src folder every time anything is pushed back to any branch. 
It can also be run manually by going to the 'Actions' tab and selecting 'github-actions-practice' which can be run with a 'workflow-dispatch' event trigger.

The requirements.txt file is very bare-bones because the code itself is bare-bones. (I added numpy and matplotlib to requirements.txt as a method of verifying that my workflow was able to install requirements). 

## Notes

I'm well-aware that there are likely a handful of extra tests I should've written, like verifying the url was getting constructed correctly, but to be honest, I found getting even this much done to be somewhat overwhelming.


## References

Sources consulted while trying to figure this out largely include the following in addition to the Docker and Flask documentation: 

https://dev.to/codemaker2015/build-and-deploy-flask-rest-api-on-docker-25mf
https://restfulapi.net/http-status-codes/
https://developers.lseg.com/en/article-catalog/article/getting-start-unit-test-for-an-http-rest-application-with-python
https://medium.com/@oyetoketoby80/how-to-write-unit-test-for-your-rest-api-f8f71376273f
https://auth0.com/blog/developing-restful-apis-with-python-and-flask/

While I did Google other things and reference some of the in-class work, I'm not sure that those things helped or informed what I did.