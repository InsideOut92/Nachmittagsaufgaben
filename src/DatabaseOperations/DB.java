package DatabaseOperations;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DB {
    public static Connection adminconnect() throws SQLException {

        try{
            var dbUrl = DatabaseConfig.getDBUrl();
            var admin = DatabaseConfig.getAdminName();
            var apass = DatabaseConfig.getAdminPassword();

            return DriverManager.getConnection(dbUrl, admin, apass);
        } catch (SQLException e){
            System.out.println(e.getMessage());
            return null;
        }
    }

    public static Connection userconnect() throws SQLException {

        try{
            var dbUrl = DatabaseConfig.getDBUrl();
            var user = DatabaseConfig.getUsername();
            var userPass = DatabaseConfig.getUserPassword();

            return DriverManager.getConnection(dbUrl, user, userPass);
        } catch (SQLException e){
            System.out.println(e.getMessage());
            return null;
        }
    }
}
