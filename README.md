# lyftApprenticeChallenge

This is the technical sample for the  Lyft Software Engineering Apprenticeship.

## Technical Sample:

Please write a small web application in one of the above languages (Python/Ruby/Javascript). The application only needs to do the following:
Accept a POST request to the route “/test”, which accepts one argument “string_to_cut”
Return a JSON object with the key “return_string” and a string containing every third letter from the original string
(e.g.) If you POST {"string_to_cut": "iamyourlyftdriver"}, it will return: {"return_string": "muydv"}.

Note: To see expected behavior you can test against a current working example with the command: curl -X POST https://lyft-interview-test.glitch.me/test --data '{"string_to_cut": "iamyourlyftdriver"}' -H 'Content-Type: application/json'

To test this locally, run the command:
curl -X POST http://localhost:5000/test --data '{"string_to_cut": "iamyourlyftdriver"}' -H 'Content-Type: application/json'

You can change the value of the string_to_cut key to any value.

I used the Flask Framework and created a Lyft resource that inherits from the Resource class. I overrode the post method and returned the appropriate Json. I used the interface reqparse to parse the args given and sliced up the resulting string so it only gave every third letter.

