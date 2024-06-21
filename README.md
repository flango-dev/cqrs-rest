# cqrs-rest

An example how to create a RESTful API suitable for CQRS.

# Run the demo

- `just project-setup`
- `just project-run`

admin user: `admin`
admin pwd: `pwd`

RESTful API v1 of both bounded contexts (A and B): `http://127.0.0.1:8000/api/v1/docs`
RESTful API v2 of bounded contexts (A and B): `http://127.0.0.1:8000/api/v2/docs`

## Notes

Bounded context A defines commands and queries in the endpoint URI.
Bounded context B defines commands and queries in the body of the request.
Never run APis in production without [authentication](https://django-ninja.dev/guides/authentication/).

## References and inspiration

- [stackoverflow - RESTful API Design and CQRS (accepted answer)](https://stackoverflow.com/a/48141654/5308983)
- [ReST vs CQRS: The Trigger Pattern](https://hawkins6423.github.io)
- [stackoverflow - What is the difference between PUT, POST and PATCH? (most liked answer)](https://stackoverflow.com/a/40711235/5308983)
