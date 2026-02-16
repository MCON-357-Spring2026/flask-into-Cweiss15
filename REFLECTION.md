1. What does the @app.route() decorator actually do?
    Connects the URL to the action
2. How does Flask know which function to call when a request arrives?
    It reads the URL and compares it to the routing file to find the right function
3. What's the difference between route parameters (<name>) and query parameters (?key=value)?
    The parameters are part of the URL and are required the query parameters are optional 
4. Why do we need to use request.get_json() for POST requests but request.args.get() for GET query parameters?
    Because their different parts of the request. GET sends info that flask parses but post is sent to request body and isn't parsed by Flask
5. What happens if you try to access request.args outside of a request context?
    You get a runtime error, it can only be accessed in requests