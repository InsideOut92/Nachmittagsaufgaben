package GUI;

import Klassen.Address;

import javax.swing.*;
import java.awt.*;

public class AddressPanel extends Panel {
    JPanel panel = new JPanel();
    JLabel streetLabel = new JLabel();
    JLabel hnrLabel = new JLabel();
    JLabel plzLabel = new JLabel();
    JLabel cityLabel = new JLabel();
    JLabel countryLabel = new JLabel();

    BoxLayout boxLayout = new BoxLayout(panel, BoxLayout.X_AXIS);

    public AddressPanel(){}

    public AddressPanel(Address address){

        this.streetLabel.setText(address.getStreet());
        this.hnrLabel.setText(address.getHnr());
        this.plzLabel.setText(address.getPlz());
        this.cityLabel.setText(address.getCity());
        this.countryLabel.setText(address.getCountry());

        panel.add(this.streetLabel);
        panel.add(this.hnrLabel);
        panel.add(this.plzLabel);
        panel.add(this.cityLabel);
        panel.add(this.countryLabel);

        this.add(panel);
    }



}
