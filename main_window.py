from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QComboBox, QPushButton, QFrame, QMessageBox
)
from PyQt6.QtGui import QDoubleValidator
from PyQt6.QtCore import QLocale
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import mplcursors
from datetime import datetime
from modules import CURRENCIES, get_rate, get_historical_rates


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ConvertIT")
        self.setFixedSize(600, 520)
        self.setup_ui()
        self.update_chart(
            self.from_currency.currentText(),
            self.to_currency.currentText()
        )

    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        calc_layout = QVBoxLayout()
        calc_layout.setSpacing(10)

        row1 = QHBoxLayout()
        self.input_amount = QLineEdit(placeholderText="Kwota wejściowa")
        self.input_amount.setValidator(QDoubleValidator())
        self.input_amount.setText("1")
        self.from_currency = QComboBox()
        self.from_currency.addItems(CURRENCIES)
        self.from_currency.setCurrentText("PLN")
        row1.addWidget(self.input_amount)
        row1.addWidget(self.from_currency)
        calc_layout.addLayout(row1)

        row2 = QHBoxLayout()
        self.convert_button = QPushButton("Przelicz")
        self.swap_button = QPushButton("⇄")
        self.swap_button.setObjectName("swap_button")
        self.convert_button.clicked.connect(self.convert)
        self.swap_button.clicked.connect(self.swap)
        row2.addWidget(self.convert_button)
        row2.addWidget(self.swap_button)
        calc_layout.addLayout(row2)

        row3 = QHBoxLayout()
        self.output_amount = QLineEdit(placeholderText="Kwota wyjściowa")
        self.output_amount.setReadOnly(True)
        self.to_currency = QComboBox()
        self.to_currency.addItems(CURRENCIES)
        self.to_currency.setCurrentText("EUR")
        row3.addWidget(self.output_amount)
        row3.addWidget(self.to_currency)
        calc_layout.addLayout(row3)

        main_layout.addLayout(calc_layout)

        self.chart_frame = QFrame()
        self.chart_frame.setFixedHeight(260)
        main_layout.addWidget(self.chart_frame)

        self.fig, self.ax = plt.subplots(figsize=(6, 3), dpi=100)
        self.fig.patch.set_facecolor('#1b1b1d')
        self.ax.set_facecolor('#242426')
        self.ax.tick_params(colors='#f2f2f3')
        for spine in self.ax.spines.values():
            spine.set_color('#3d3d40')

        self.canvas = FigureCanvas(self.fig)
        self.canvas.setStyleSheet("background: transparent;")

        lay = QVBoxLayout(self.chart_frame)
        lay.setContentsMargins(10, 10, 10, 10)
        lay.addWidget(self.canvas)

    def convert(self):
        raw = self.input_amount.text().replace(",", ".")
        try:
            amount = float(raw)
        except ValueError:
            QMessageBox.warning(self)
            return

        base = self.from_currency.currentText()
        target = self.to_currency.currentText()

        rate = get_rate(base, target)
        if rate is None:
            QMessageBox.critical(self)
            return

        result = amount * rate
        self.output_amount.setText(
            QLocale.system().toString(result, 'f', 2)
        )
        self.update_chart(base, target)

    def swap(self):
        i = self.from_currency.currentIndex()
        j = self.to_currency.currentIndex()
        self.from_currency.setCurrentIndex(j)
        self.to_currency.setCurrentIndex(i)
        self.convert()

    def update_chart(self, base, target):
        dates, rates = get_historical_rates(base, target)
        if not dates:
            return

        dt_dates = [datetime.fromisoformat(d) for d in dates]
        x_vals = list(range(len(rates)))

        self.ax.clear()

        self.ax.plot(x_vals, rates, color='#2188ff', linewidth=2)
        sc = self.ax.scatter(
            x_vals, rates, s=15,
            facecolors='#1b1b1d', edgecolors='#2188ff',
            linewidths=1, zorder=5
        )
        cursor = mplcursors.cursor(sc, hover=True)

        @cursor.connect("add")
        def on_add(sel):
            idx = sel.index
            date_str = dt_dates[idx].strftime('%d.%m.%Y')
            sel.annotation.set_text(f"{date_str}\n{rates[idx]:.5f}")
            sel.annotation.set_color('#ffffff')
            sel.annotation.get_bbox_patch().set(fc="#1b1b1d", ec="#2188ff")

        tick_positions = list(range(0, len(dt_dates), 3))
        tick_labels = [dt_dates[i].strftime('%d.%m') for i in tick_positions]
        self.ax.set_xticks(tick_positions)
        self.ax.set_xticklabels(tick_labels, ha='right', color='#bbbbbb')

        self.ax.set_title(
            f"1 {base} → 1 {target} (ostatnie 30 dni)", color='#f2f2f3')
        self.ax.grid(True, linestyle='--', alpha=0.4, color='#3d3d40')
        for label in self.ax.get_yticklabels():
            label.set_color('#bbbbbb')

        self.canvas.draw()
