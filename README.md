# SC-FIRST-Strategy-API
The SC FIRST Strategy API allows applications to verify team and match data using The Blue Alliance API and to submit results to an online database/document.

## Table of Contents
- [GET Examples](#get-examples)
- [POST Examples](#post-examples)
- More features TBD


## GET Examples
----
#### Python
```py
import requests

url = "https://scfirst5436-strategy-806036691402.us-central1.run.app/"

params = {
    "type":"team"
}

response = requests.get(
    url,
    headers={
        "Content-Type": "application/json",
        "X-SCF-API-KEY": "TEAM_API_KEY" #not the TBA one
    },
    params=params
)

print("Status code:", response.status_code)
print("Response body:", response.text)
```
For python, you can just copy and paste this code in order to make it work!

#### Java
```java
package maven.poje;

import kong.unirest.HttpResponse;
import kong.unirest.Unirest;

public class App {
    public static void main(String[] args) {
        String TEAM_API_KEY = "TEAM_API_KEY"; // Again, not the TBA one

        HttpResponse<String> response = Unirest.get("https://scfirst5436-strategy-806036691402.us-central1.run.app/")
                .header("Content-Type", "application/json")
                .header("X-SCF-API-KEY", TEAM_API_KEY)
                .queryString("type", "team") 
                .asString();

        System.out.println("Status code: " + response.getStatus());
        System.out.println("Response body: " + response.getBody());
    }
}
```
- Remember that Java is not the same as python. You need to have a Maven type project with the `com.konghq` library inside your `pom.xml` file to make it work. You can get the library here: [Get Unirest Library](https://mvnrepository.com/artifact/com.konghq/unirest-java/4.0.0-RC2)
- Remember to change `public class App {` to whatever your .java file is named
- Aaand remember to change `package maven.poje;` to whatever your project file is named

Both of these codes **GET** a random list of values from TBA API

## POST Examples
----
#### Python
```py
import requests

url = "https://scfirst5436-strategy-806036691402.us-central1.run.app/"

payload = {
    "team_number":"frc1234",
    "event_type":"sctest"
}

response = requests.post(
    url,
    headers={
        "Content-Type": "application/json",
        "X-SCF-API-KEY": "TEAM_API_KEY" #not the TBA one
    },
    json=payload
)

print("Status code:", response.status_code)
print("Response body:", response.text)
```
For python, you can just copy and paste this code in order to make it work!

#### Java
```java
package maven.poje;

import kong.unirest.HttpResponse;
import kong.unirest.Unirest;

public class App {
    public static void main(String[] args) {
        String TEAM_API_KEY = "TEAM_API_KEY"; // Not TBA key
        String url = "https://scfirst5436-strategy-806036691402.us-central1.run.app/";

        // We create a JSON with some values
        String jsonPayload = "{ \"team_number\": \"frc1234\", \"event_type\": \"sctest\" }";

        // Send POST request through ->
        HttpResponse<String> response = Unirest.post(url)
                .header("Content-Type", "application/json")
                .header("X-SCF-API-KEY", TEAM_API_KEY)
                .body(jsonPayload)  // JSON payload very important!11!1
                .asString();

        System.out.println("Status code: " + response.getStatus());
        System.out.println("Response body: " + response.getBody());
    }
}
```
- Remember that Java is not the same as python. You need to have a Maven type project with the `com.konghq` library inside your `pom.xml` file to make it work. You can get the library here: [Get Unirest Library](https://mvnrepository.com/artifact/com.konghq/unirest-java/4.0.0-RC2)
- Remember to change `public class App {` to whatever your .java file is named
- Finally, remember to change `package maven.poje;` to whatever your project file is named

Both of these codes **POST** a json file. Currently, this feature only makes the server return the json received.
