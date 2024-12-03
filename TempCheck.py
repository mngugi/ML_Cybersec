import psutil

def get_temperature_linux():
    try:
        sensors = psutil.sensors_temperatures()
        if "coretemp" in sensors:
            for sensor in sensors["coretemp"]:
                print(f"{sensor.label or 'CPU Core'}: {sensor.current}°C")
        else:
            print("No core temperature data available.")
    except Exception as e:
        print("Error:", e)

get_temperature_linux()

