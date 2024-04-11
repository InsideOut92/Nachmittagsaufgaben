package SQL;

import DatabaseOperations.DB;
import Klassen.Address;
import Klassen.Presents;

import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class SelectStmt {

    public static ArrayList<Address> findAllAddresses(){
        var addresses = new ArrayList<Address>();

        var sql = "SELECT * FROM address";

        try(
                var conn = DB.userconnect();
                var stmt = conn.createStatement()
                ){
            var resultSet = stmt.executeQuery(sql);

            while(resultSet.next()){
                var address = new Address(
                        resultSet.getInt("addressid"),
                        resultSet.getString("street"),
                        resultSet.getString("hnr"),
                        resultSet.getString("plz"),
                        resultSet.getString("city"),
                        resultSet.getString("country")
                );
                addresses.add(address);
            }
        } catch (SQLException e){
            e.printStackTrace();
        }

        return addresses;
    }

    public static List<Presents> findAllPresents(){
        var presents = new ArrayList<Presents>();

        var sql = "SELECT * FROM presents";

        try(
                var conn = DB.userconnect();
                var stmt = conn.createStatement()
        ){
            var resultSet = stmt.executeQuery(sql);

            while(resultSet.next()){
                var present = new Presents(
                        resultSet.getInt("presentid"),
                        resultSet.getString("description"),
                        resultSet.getString("color")
                );
                presents.add(present);
            }
        } catch (SQLException e){
            e.printStackTrace();
        }

        return presents;
    }

    public static void main(String[] args) {
        List<Address> adresses = findAllAddresses();

       for(int i = 0; i < adresses.size() - 1; i++){
           System.out.println(adresses.get(i));
        }

    }
}
