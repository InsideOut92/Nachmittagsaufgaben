import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.Assertions;

public class TraktorTest {
    private Traktor traktor;

    @BeforeEach
    void setUp(){
        traktor = new Traktor(98, 67, 4.5, 80, 15,
                "S-OL 1", "rot", "Hubsi", 230456, 3, false,
                406590, 86.2, false, 23.4);
    }

    @Test
    void testSetUp(){
        Assertions.assertAll("default traktor",
                () -> Assertions.assertEquals(98.0, traktor.getTankvolumen()),
                () -> Assertions.assertEquals(67.0, traktor.getTankinhalt()),
                () -> Assertions.assertEquals("Hubsi", traktor.getDriver()),
                () -> Assertions.assertFalse(traktor.isFueling())
        );
    }

    // Test 1: Ob die beiden Variablen korrekt befüllt werden
    @Test
    void testTraktorConstructor() {
        Traktor traktor = new Traktor(true, 30.5);

        Assertions.assertAll("Traktor constructor",
                () -> Assertions.assertTrue(traktor.isFrontlader()),
                () -> Assertions.assertEquals(30.5, traktor.getLadung(), 0.0)
        );
    }

    // Test 2: Eigentlich sollte die Ladung nicht negativ sein dürfen
    @Test
    void testTraktorConstructorNegativeLadung() {
        Traktor traktor = new Traktor(true, -5.0);

        Assertions.assertAll("Traktor constructor with negative ladung",
                () -> Assertions.assertTrue(traktor.isFrontlader()),
                () -> Assertions.assertEquals(0.0, traktor.getLadung(), 0.0)  // Ladung sollte auf 0 gesetzt werden
        );
    }

    // Test für die Konstruktor-Anforderung
    @Test
    void testTraktorConstructor() {
        Traktor traktor = new Traktor(true, 20.5);

        Assertions.assertAll("Traktor constructor",
                () -> Assertions.assertTrue(traktor.isFrontlader()),
                () -> Assertions.assertEquals(20.5, traktor.getLadung(), 0.0)
        );
    }

    // Test für die Full-Constructor-Anforderung
    @Test
    void testTraktorFullConstructor() {
        Traktor traktor = new Traktor(80, 60, 5.0, 70, 45,
                "T-KT 567", "blau", "John", 120.5, 100.0,
                75.5, true, 15.3);

        Assertions.assertAll("Traktor full constructor",
                () -> Assertions.assertEquals(80.0, traktor.getTankvolumen()),
                () -> Assertions.assertEquals(60.0, traktor.getTankinhalt()),
                () -> Assertions.assertEquals(5.0, traktor.getVebrauch(), 0.0),
                () -> Assertions.assertEquals(70.0, traktor.getMaxSpeed()),
                () -> Assertions.assertEquals(45.0, traktor.getCurrentSpeed()),
                () -> Assertions.assertEquals("T-KT 567", traktor.getKennzeichen()),
                () -> Assertions.assertEquals("blau", traktor.getColor()),
                () -> Assertions.assertEquals("John", traktor.getDriver()),
                () -> Assertions.assertEquals(120.5, traktor.getStrecke(), 0.0),
                () -> Assertions.assertEquals(100.0, traktor.getMoney(), 0.0),
                () -> Assertions.assertEquals(75.5, traktor.getReifenProzent(), 0.0),
                () -> Assertions.assertTrue(traktor.isFrontlader()),
                () -> Assertions.assertEquals(15.3, traktor.getLadung(), 0.0),
                () -> Assertions.assertFalse(traktor.isFueling()),  // Extra Test for isFueling
                () -> Assertions.assertTrue(traktor.getRennstrecke() <= traktor.getStrecke())  // Extra Test for rennstrecke
        );
    }

    // Test: Ob alle Variablen korrekt befüllt werden
    @Test
    void testTraktorExtendedConstructor_validValues() {
        Traktor traktor = new Traktor(80.0, 75.0, 5.0, 70.0, 60.0,
                "XYZ-123", "Blau", "Fritz", 120.0, 100.0, true,
                500.0, 85.0, false, 45.7);

        Assertions.assertAll("Traktor extended constructor with valid values",
                () -> Assertions.assertEquals(80.0, traktor.getTankvolumen())
        );
    }

    // Test: Wenn versucht wird, tankinhalt > tankvolumen; currentSpeed > maxSpeed; rennstrecke
    @Test
    void testTraktorExtendedConstructor_invalidTankValues() {
        // Ensure that an IllegalArgumentException is thrown for invalid tank values
        Assertions.assertThrows(IllegalArgumentException.class, () ->
                new Traktor(-10.0, 75.0, 5.0, 70.0, 60.0,
                        "XYZ-123", "Blau", "Fritz", 120.0, 100.0, true,
                        500.0, 85.0, false, 45.7));
    }

    // Test: Negative Werte
    @Test
    void testTraktorExtendedConstructor_negativeValues() {
        // Ensure that an IllegalArgumentException is thrown for negative values
        Assertions.assertThrows(IllegalArgumentException.class, () ->
                new Traktor(80.0, -75.0, -5.0, 70.0, -60.0,
                        "XYZ-123", "Blau", "Fritz", -120.0, -100.0, true,
                        -500.0, -85.0, true, -45.7));
    }

    // Test: Ob Methode funktioniert
    @Test
    void testIsFrontlader() {
        // Test: Ob Methode funktioniert
        Traktor traktor = new Traktor(true, 30.5);
        Assertions.assertTrue(traktor.isFrontlader());
    }

    // Test mit true
    @Test
    void testSetFrontladerTrue() {
        Traktor traktor = new Traktor();
        traktor.setFrontlader(true);
        Assertions.assertTrue(traktor.isFrontlader());
    }

    // Test mit false
    @Test
    void testSetFrontladerFalse() {
        Traktor traktor = new Traktor();
        traktor.setFrontlader(false);
        Assertions.assertFalse(traktor.isFrontlader());
    }

    // Test ob die Methode funktioniert
    @Test
    void testGetLadung() {
        Traktor traktor = new Traktor(false, 42.0);
        Assertions.assertEquals(42.0, traktor.getLadung(), 0.0);
    }

    // Test mit positivem Wert
    @Test
    void testSetLadungPositiv() {
        Traktor traktor = new Traktor(false, 0.0);
        traktor.setLadung(15.3);
        Assertions.assertEquals(15.3, traktor.getLadung(), 0.0);
    }

    // Test mit negativem Wert
    @Test
    void testSetLadungNegativ() {
        Traktor traktor = new Traktor(false, 0.0);
        traktor.setLadung(-5.2);
        Assertions.assertEquals(-5.2, traktor.getLadung(), 0.0);
    }

    // Test mit Grenzwert
    @Test
    void testSetLadungMaxDoublePlusOne() {
        Traktor traktor = new Traktor(false, 0.0);
        traktor.setLadung(Double.MAX_VALUE + 1);
        Assertions.assertEquals(Double.MAX_VALUE + 1, traktor.getLadung(), 0.0);
    }

    // Test von Grenzwert mit realistischen Werten
    @Test
    void testSetLadungRealisticRange() {
        Traktor traktor = new Traktor(false, 0.0);
        traktor.setLadung(25.7);
        Assertions.assertEquals(25.7, traktor.getLadung(), 0.0);
    }

    // Test ob Geschwindigkeit und Ausgabe stimmen
    @Test
    void testProtestieren() {
        Traktor traktor = new Traktor(true, 0.0);
        traktor.protestieren();
        Assertions.assertEquals(0.0, traktor.getCurrentSpeed(), 0.0);
    }
}
