package GUI;

import Klassen.Address;
import Klassen.Presents;

import javax.swing.*;
import java.awt.*;

public class PresentPanel extends Panel {
    JPanel panel = new JPanel();
    JLabel descriptionLabel = new JLabel();
    JLabel colorLabel = new JLabel();

    BoxLayout boxLayout = new BoxLayout(panel, BoxLayout.X_AXIS);

    public PresentPanel(){}

    public PresentPanel(Presents present){
        this.descriptionLabel.setText(present.getDescription());
        this.colorLabel.setText(present.getColor());

        this.panel.add(descriptionLabel);
        this.panel.add(colorLabel);

        this.add(panel);
    }



}
