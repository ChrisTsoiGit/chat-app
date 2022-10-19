AccountIn{
username*	Username[]
email*	Email[]
password*	Password[]
full_name*	Full Name[]
 
}

AccountOut{
id*	Id[]
username*	Username[]
email*	Email[]
full_name*	Full Name[]
 
}

AccountToken{
description:	
Represents a bearer token.

access_token*	Access Token[]
token_type	Token Type[]
account*	AccountOut{}
 
}

Body_login_token_post{
grant_type	Grant Type[]
username*	Username[]
password*	Password[]
scope	Scope[]
client_id	Client Id[]
client_secret	Client Secret[]
 
}

Token{
description:	
Represents a bearer token.

access_token*	Access Token[]
token_type	Token Type[]
 
}



