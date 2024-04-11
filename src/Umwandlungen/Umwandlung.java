package Umwandlungen;

import java.sql.Date;
import java.util.Calendar;

public class Umwandlung {

    public static Date dateUmwandlung(java.util.Date date){
        Calendar cal = Calendar.getInstance();
        cal.set(Calendar.YEAR, date.getYear());
        cal.set(Calendar.MONTH, date.getMonth());
        cal.set(Calendar.DAY_OF_MONTH, date.getDay());

        return new Date(cal.getTimeInMillis());
    }
}
