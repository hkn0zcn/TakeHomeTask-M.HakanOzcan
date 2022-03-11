import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import io.restassured.response.Response;
import io.restassured.response.ResponseBody;
import io.restassured.specification.RequestSpecification;
import org.testng.Assert;
import org.testng.annotations.Test;

import static io.restassured.RestAssured.given;
import static io.restassured.RestAssured.when;
import static org.hamcrest.Matchers.equalTo;
import static org.hamcrest.Matchers.lessThan;

public class RestAssuredTest {


    @Test
    public void test_UserLogout() {
        RestAssured.baseURI = "https://petstore.swagger.io";
        RequestSpecification httpRequest = given();
        Response response = httpRequest.get("/v2/user/logout");
        ResponseBody body = response.getBody();
        String bodyAsString = body.asString();
        System.out.println(bodyAsString);
        Assert.assertTrue(bodyAsString.contains("ok"),"string did not found");
    }

    @Test
    public void test_FindByStatusSold() {
        when()
                .get("https://petstore.swagger.io/v2/pet/findByStatus?status=sold")
                .then()
                .statusCode(200)
                .time(lessThan(2000L));
    }

    @Test
    public void test_NonexistentID() {
      when()
              .get("https://petstore.swagger.io/v2/pet/1994")
              .then()
              .statusCode(404)
              .body("message",equalTo("Pet not found"))
              .time(lessThan(2000L));
    }

    @Test
    public void test_AddANewPet() {
      String postData = "{\n" +
              "\"id\": \"1\",\n" +
              "\"category\": {\n" +
                      " \"id\":\"0\",\n" +
                      " \"name\":\"string\"},\n" +
              "\"name\":\"Mybird\",\n"+
              "\"photoUrls\":[\n"+
              "      \"string\"],\n"+
              "\"tags\": [\n"+
                    "{\"id\": \"0\",\n"+
                    "\"name\":\"string\"}],\n"+
              "\"status\":\"available\""+
    "}";

      given().
              contentType(ContentType.JSON).
              body(postData).
              when().
              post("https://petstore.swagger.io/v2/pet").
              then().
              statusCode(200).
              body("name",equalTo("Mybird")).
              time(lessThan(2000L));
    }

    @Test
    public void testStoreOrder() {
        String postData = "{\n" +
                " \"id\": \"1\",\n" +
                " \"petId\": \"1\",\n" +
                " \"quantiy\": \"1\",\n" +
                " \"shipDate\": \"2022-03-10T06:30:14.884Z\",\n" +
                "\"status\": \"placed\",\n"+
                "\"complete\": \"true\"\n"+
                "}";
        given().
                contentType(ContentType.JSON).
                body(postData).
                when().
                post("https://petstore.swagger.io/v2/store/order").
                then().
                statusCode(200).
                body("status",equalTo("placed")).
                body("complete",equalTo(true)).
                time(lessThan(2000L));
    }
}
