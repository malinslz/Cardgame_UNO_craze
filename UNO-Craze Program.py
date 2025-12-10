from time import sleep, ticks_ms, ticks_diff
import urandom

# -----------------------------------------
# Modulino Hardware
# -----------------------------------------
from modulino import ModulinoButtons, ModulinoBuzzer, ModulinoDistance
from machine import I2C, SoftI2C, Pin
from lcd_i2c import LCD
from i2c_lcd import RGBDisplay


# -----------------------------------------------------------------
#                         SETUP
# -----------------------------------------------------------------

# --- Buzzer ---
buzzer = ModulinoBuzzer()

# --- Start-Melodie ---
def start_melody():
    notes = [262, 330, 392, 523]  # C – E – G – C
    duration = 0.15
    for n in notes:
        buzzer.tone(n)
        sleep(duration)
    buzzer.tone(0)

start_melody()   # >>> Melodie beim Start


# --- Buttons ---
buttons = ModulinoButtons()

# --- I2C Bus (LCD + RGB Display) ---
i2c_bus = I2C(1, scl=Pin("D8"), sda=Pin("D9"))

# --- LCD Pfeil-Display ---
lcd_arrow = LCD(0x27, 16, 2, i2c=i2c_bus)
lcd_arrow.begin()
lcd_arrow.clear()

# --- RGB Display ---
rgb_button = Pin("A1", Pin.IN, Pin.PULL_UP)
display_rgb = RGBDisplay(i2c_bus)
display_rgb.clear()
rgb_prev = rgb_button.value()
colors = [(255,0,0), (0,255,0), (0,0,255), (255,255,0)]
numbers = ["1","2","3","4"]


# -----------------------------------------------------------------
#             DISTANZSENSOREN (4 Spieler inkl. RX/TX)
# -----------------------------------------------------------------

# Player 4 – SoftI2C an A2/A3
g1_scl = Pin("A2", Pin.OPEN_DRAIN, Pin.PULL_UP)
g1_sda = Pin("A3", Pin.OPEN_DRAIN, Pin.PULL_UP)
soft_i2c1 = SoftI2C(scl=g1_scl, sda=g1_sda, freq=100000)
distance_g1 = ModulinoDistance(soft_i2c1)

# Player 3 – Qwiic über I2C(0)
i2c0 = I2C(0, freq=100000)
distance_qwiic = ModulinoDistance(i2c0)

# Player 2 – SoftI2C an D5/D6
g2_scl = Pin("D5", Pin.OPEN_DRAIN, Pin.PULL_UP)
g2_sda = Pin("D6", Pin.OPEN_DRAIN, Pin.PULL_UP)
i2c1 = SoftI2C(scl=g2_scl, sda=g2_sda, freq=100000)
distance_g0 = ModulinoDistance(i2c1)

# Player 1 – NEU: Sensor an RX/TX
rx_scl = Pin("RX", Pin.OPEN_DRAIN, Pin.PULL_UP)
tx_sda = Pin("TX", Pin.OPEN_DRAIN, Pin.PULL_UP)
i2c_rx_tx = SoftI2C(scl=rx_scl, sda=tx_sda, freq=100000)
distance_rx_tx = ModulinoDistance(i2c_rx_tx)

# Sensorliste in Anzeige-Reihenfolge
sensors = [
    distance_rx_tx,  # Player 1
    distance_qwiic,  # Player 3
    distance_g0,     # Player 2
    distance_g1      # Player 4
]

PLAYER_NAMES = ["Player 1", "Player 3", "Player 2", "Player 4"]
DISPLAY_DISTANCE = 3.0


# -----------------------------------------------------------------
#                        FUNKTIONEN
# -----------------------------------------------------------------

# ----- Pfeil-Button -----
arrow_active = False
arrow_end_time = 0

def trigger_arrow():
    global arrow_active, arrow_end_time
    arrow_text = urandom.choice(["-->", "<--"])
    lcd_arrow.clear()
    lcd_arrow.print(arrow_text)
    arrow_active = True
    arrow_end_time = ticks_ms() + 1600

buttons.on_button_b_press = lambda: trigger_arrow()

# ----- RGB Display Knopf -----
def rgb_display_pressed():
    index = urandom.getrandbits(8) % 4
    r, g, b = colors[index]
    display_rgb.color(r, g, b)
    display_rgb.clear()
    display_rgb.write(numbers[index])

# ----- Distanzsensoren prüfen -----
def update_distance_display():
    if arrow_active:
        return

    for i, sensor in enumerate(sensors):
        distance = sensor.distance  # Falls erforderlich → Methode anpassen
        if distance <= DISPLAY_DISTANCE:
            lcd_arrow.clear()
            lcd_arrow.print(f"{PLAYER_NAMES[i]}: {distance:.1f}cm")
            return True

    lcd_arrow.clear()
    return False


# -----------------------------------------------------------------
#                        HAUPTSCHLEIFE
# -----------------------------------------------------------------

while True:
  
    # --- RGB Button ---
    val = rgb_button.value()
    if val == 0 and rgb_prev == 1:
        rgb_display_pressed()
    rgb_prev = val

    # --- Buttons update ---
    buttons.update()

    # --- Arrow auto-clear ---
    if arrow_active and ticks_diff(ticks_ms(), arrow_end_time) >= 0:
        lcd_arrow.clear()
        arrow_active = False

    # --- Distanzsensoren prüfen ---
    update_distance_display()

    sleep(0.02)
