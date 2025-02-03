import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class AdvancedCalculator {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Erweiterter Taschenrechner");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(250, 300);
        frame.setResizable(false);
        // Erstelle ein Panel mit GridBagLayout für die Tasten
        JPanel panel = new JPanel(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.fill = GridBagConstraints.BOTH;
        gbc.insets = new Insets(2, 2, 2, 2); // Abstand zwischen den Komponenten

        // Erstelle ein Textfeld zur Anzeige der Eingabe und des Ergebnisses
        JTextField display = new JTextField();
        display.setEditable(false);
        display.setHorizontalAlignment(JTextField.RIGHT);

        // Füge das Display hinzu
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.gridwidth = 4;
        panel.add(display, gbc);

        // Erstelle eine Textarea für Meldungen
        JTextArea messageArea = new JTextArea(5, 20);
        messageArea.setEditable(false);
        JScrollPane scrollPane = new JScrollPane(messageArea);
        gbc.gridy = 6;
        panel.add(scrollPane, gbc);

        // Erstelle die Tasten
        String[] buttonTexts = {
            "7", "8", "9", "+",
            "4", "5", "6", "-",
            "1", "2", "3", "=",
            "0"
        };

        // Positionen für die Tasten
        int[][] positions = {
            {2, 0}, {2, 1}, {2, 2}, {2, 3},
            {3, 0}, {3, 1}, {3, 2}, {3, 3},
            {4, 0}, {4, 1}, {4, 2}, {4, 3},
            {5, 0} // "0" Taste
        };

        // Füge die Tasten hinzu
        for (int i = 0; i < buttonTexts.length; i++) {
            JButton button = new JButton(buttonTexts[i]);
            gbc.gridx = positions[i][1];
            gbc.gridy = positions[i][0];

            // "0" Taste soll sich über zwei Spalten erstrecken
            if ("0".equals(buttonTexts[i])) {
                gbc.gridwidth = 2;
            } else {
                gbc.gridwidth = 1;
            }

            panel.add(button, gbc);

            // Füge ActionListener zu den Tasten hinzu
            button.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    String command = e.getActionCommand();
                    messageArea.append("Taste '" + command + "' wurde gedrückt\n");
                    if ("=".equals(command)) {
                        display.setText("Ergebnis");
                    } else {
                        display.setText(display.getText() + command);
                    }
                }
            });
        }

        // Füge das Panel dem Frame hinzu
        frame.setLayout(new BorderLayout());
        frame.add(panel, BorderLayout.CENTER);

        // Zeige das Fenster
        frame.setVisible(true);
    }
}
