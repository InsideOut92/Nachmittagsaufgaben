package DatabaseOperations;

import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

public class DatabaseConfig {
    private static final Properties properties = new Properties();

    static {
        try (InputStream input = DatabaseConfig.class.getClassLoader().getResourceAsStream("DatabaseOperations/db.properties")){
            if (input == null){
                System.out.println("Entschuldige, ich konnte die Datei db.properties nicht laden");
            }
            properties.load(input);
        } catch (IOException e){
            e.printStackTrace();
        }
    }

    public static String getDBUrl(){
        return properties.getProperty("db.url");
    }

    public static String getAdminName(){
        return properties.getProperty("db.adminName");
    }

    public static String getAdminPassword(){
        return properties.getProperty("db.adminPassword");
    }

    public static String getUsername(){
        return properties.getProperty("db.username");
    }

    public static String getUserPassword(){
        return properties.getProperty("db.userPassword");
    }

    /*
    public static void main(String[] args){
        System.out.println("URL: " + getDBUrl());
        System.out.println("AdminName: " + getAdminName());
        System.out.println("AdminPass: " + getAdminPassword());
        System.out.println("Username: " + getUsername());
        System.out.println("Userpass: " + getUserPassword());
    }
    */
}
