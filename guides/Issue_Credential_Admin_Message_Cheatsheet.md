# Workshop Cheatsheet
## Issue Credential Admin Messages

This cheatsheet contains example message types that you can use to issue credentials to agent connections. 

Note: In order to send these messages, the static agent connection must have the 'admin' role.



### Return Routing

Each message you send may need a `~transport` `return_route` option specified. This can be done using a library option if it provides one, or by including it directly as shown :

```json
{
  "@type": "example_message_type",
  "~transport": {
    "return_route": "all"
  },
  "other": "message attributes"
}
```

The examples below include it to help prevent issues, but you may remove it if your library provides this feature.

### Connections

```json
// Connection Get List
{
  "@type": "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/admin-connections/1.0/connection-get-list",
  "~transport": {
    "return_route": "all"
  }
}
```

```json
// Example Response
{
    "@type": "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/admin-connections/1.0/connection-list",
    "@id": "a9329971-ad7c-498b-bf16-a8b2b71b994a",
    "~thread": {
        "thid": "1569250789667"
    },
    "results": [
        {
            "initiator": "self",
            "my_did": "VZLav48HF5m12hqFrXhWo9",
            "invitation_mode": "once",
            "their_role": "admin",
            "invitation_key": "J4s5XXwwKSXx1fZt2kKKUCz7Pgexjwycp1HhUSXvi6V4",
            "their_label": "ToolBox",
            "state": "active",
            "created_at": "2019-09-23 14:59:05.246758Z",
            "routing_state": "none",
            "accept": "auto",
            "updated_at": "2019-09-23 14:59:40.105125Z",
            "connection_id": "76bd89f3-a4ac-4578-bc95-f4d1703793b5",
            "their_did": "VmMvU6eKtwP9hd1KTFvAZF"
        }
    ]
}
```

### Credential Definitions
```json
// request a list of cred defs
{
    "@type": "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/admin-credential-definitions/1.0/credential-definition-get-list",
    "~transport": {
      "return_route": "all"
    }
}
```
```json
// list of cred defs returned
{
    "@type": "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/admin-credential-definitions/1.0/credential-definition-list",
    "~transport": {
      "return_route": "all"
    },
    "results": [
    	{
    		"cred_def_id": "",
    		"schema_id": "",
    		"attributes": ["", ""],
    		"author": ""
    	}
    ]
}
```


### Credentials

```json
{
  "@type": "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/admin-issuer/1.0/send-credential",
  "comment": "testing issuance of credential",
  "credential_definition_id": "EFMHM7uFSY1NwieV9bLMAa:3:CL:74396:default",
  "connection_id": "389beee5-b3a4-4f8e-9beb-838184c1051a",
  "credential_proposal": {
    "@type": "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/issue-credential/1.0/credential-preview",
    "attributes": [
      {
        "name": "name",
        "value": "chuck testa"
      },
      {
        "name": "age",
        "value": "30"
      }
    ]
  }
}
```

