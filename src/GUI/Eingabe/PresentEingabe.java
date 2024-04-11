package GUI.Eingabe;

import GUI.PresentPanel;
import Klassen.Presents;
import SQL.InsertStmt;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

public class PresentEingabe {
    // JFrame zur Darstellung des Eingabefensters
    JFrame frame = new JFrame("Geschenkeingabe");

    // Labels und Textfelder für die Eingabe von Beschreibung und Farbe
    JLabel descriptionLabel = new JLabel("Beschreibung: ");
    JTextField descriptionTF = new JTextField();
    JLabel colorLabel = new JLabel("Farbe: ");
    JTextField colorTF = new JTextField();

    // Panels für die Anordnung der GUI-Komponenten
    JPanel enterPanel = new JPanel();
    JPanel newEntryPanel = new JPanel();
    JPanel eingabePanel = new JPanel();

    // Liste zur Speicherung der eingegebenen Geschenke
    ArrayList<Presents> presents = new ArrayList<>();

    // Layout-Manager und Constraints für die Panels
    GridBagLayout gbl = new GridBagLayout();
    GridBagConstraints gbc = new GridBagConstraints();

    // Layout für das Panel zur Eingabe neuer Geschenke
    BoxLayout entryBoxLayout = new BoxLayout(enterPanel, BoxLayout.Y_AXIS);

    // Layout für das Hauptpanel
    BoxLayout eingabeLayout = new BoxLayout(eingabePanel, BoxLayout.Y_AXIS);

    // Button zur Übertragung der Liste in die Datenbank
    JButton execute = new JButton("Liste übertragen");
    JButton addEntry = new JButton("Eintrag hinzufügen");
    JButton abort = new JButton("Abbrechen");

    // Methode zur Erstellung des Eingabefensters und der GUI-Komponenten
    private void createFrame(){
        newEntryPanel.setLayout(gbl);
        gbl.setConstraints(newEntryPanel, gbc);

        // Hinzufügen der Beschreibungskomponenten
        gbc.gridx = 0;
        gbc.gridy = 0;
        newEntryPanel.add(descriptionLabel, gbc);

        gbc.gridx = 1;
        descriptionTF.setPreferredSize(new Dimension(70, 20));
        newEntryPanel.add(descriptionTF, gbc);

        // Hinzufügen der Farbenkomponenten
        gbc.gridx = 0;
        gbc.gridy = 1;
        newEntryPanel.add(colorLabel, gbc);

        gbc.gridx = 1;
        colorTF.setPreferredSize(new Dimension(70, 20));
        newEntryPanel.add(colorTF, gbc);

        // Hinzufügen der Buttons
        gbc.gridx = 0;
        gbc.gridy = 2;
        newEntryPanel.add(execute, gbc);

        gbc.gridx = 1;
        newEntryPanel.add(addEntry, gbc);

        gbc.gridx = 0;
        gbc.gridy = 3;
        newEntryPanel.add(abort, gbc);

        // Hinzufügen des Panels zur Gesamtoberfläche
        eingabePanel.setLayout(eingabeLayout);
        eingabePanel.add(newEntryPanel);

        enterPanel.setLayout(entryBoxLayout);
        eingabePanel.add(enterPanel);

        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        frame.add(eingabePanel);

        frame.setSize(200, 300);
        frame.setVisible(true);
    }

    // Hauptmethode zum Starten des Eingabefensters
    public void main(){
        javax.swing.SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                createFrame();
                setButtonListener();
            }
        });
    }

    // Methode zum Hinzufügen eines Geschenks zur Liste
    private void addPresent(){
        String description = this.descriptionTF.getText();
        String color = this.colorTF.getText();

        if (color.isEmpty()){
            color = null;
        }

        if (description.isEmpty()){
            JOptionPane.showMessageDialog(frame, "Bitte geben Sie eine Beschreibung ein.", "Fehler", JOptionPane.ERROR_MESSAGE);
        } else {
            Presents present = new Presents(description, color);
            presents.add(present);
            addEntries();
        }
    }

    // Methode zum Hinzufügen von Button-Action-Listenern
    private void setButtonListener(){
        ActionListener addEntryListener = new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                addPresent();
            }
        };
        addEntry.addActionListener(addEntryListener);

        ActionListener addToDatabaseListener = new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (!presents.isEmpty()) {
                    for (Presents present : presents) {
                        InsertStmt.addPresent(present);
                    }
                    frame.dispose();
                } else {
                    JOptionPane.showMessageDialog(frame, "Es wurden keine Geschenke hinzugefügt.", "Hinweis", JOptionPane.INFORMATION_MESSAGE);
                }
            }
        };
        execute.addActionListener(addToDatabaseListener);
    }

    // Methode zum Hinzufügen der eingegebenen Geschenke zur Liste auf der GUI
    private void addEntries(){
        enterPanel.removeAll();

        for(Presents present : presents){
            PresentPanel pPanel = new PresentPanel(present);
            enterPanel.add(pPanel);
        }
        enterPanel.revalidate();
        enterPanel.repaint();
    }
}
