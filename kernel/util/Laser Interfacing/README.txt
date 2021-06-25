The current IP of the DL-EN1 (laser TCP module) is 169.254.222.222 at port 64000

LaserUTIL contains functionality to communicate with the lasers

TO USE:
    Connect via Ethernet to the switch
    Create a LaserArray() object with proper host and port
    Call LaserArray object's getData() or getIndividual()
    Parse the data returned as desired


laserDemo contains an example of how one can parse the data into integers by:
    1. Split message at ','
    2. Replace '+' with '' (i.e. remove '+')
    3. Convert the string to Int
    4. Divide appropriately to create a decimal point placement (depends on settings)

DEBUG NOTES:
    If connectivity issues arise, try using the included IP tool from Keyence to set a new IP for the DL-EN1
    If it seems to be returning null data, try pining the laser numbers with send("SR,00,077", host, port)
    If issues still arise, try checking individual physical connections between the lasers