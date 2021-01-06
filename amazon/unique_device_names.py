"""
Create unique device names. If a device anme already
exists an integer number is added at the end of the name.
The integer starts with 1 and is incremented by 1, for
each new request of an existing device name.

Given a list of device name requests, process
all requests and return an array of the corresponding unique
device names.

Example: ["switch", "tv", "switch", "tv", "switch", "tv"]
return: ["switch", "tv", "switch1", "tv1", "switch2", "tv2"]
"""


def unique_device_names(devices):
    names_dict = {}
    result = []
    for d in devices:
        if d not in names_dict:
            names_dict[d] = 1
            result.append(d)
        else:
            result.append(d + str(names_dict[d]))
            names_dict[d] += 1
    return result


if __name__ == "__main__":
    assert unique_device_names(["switch", "tv", "switch", "tv", "switch", "tv"]) == [
        "switch",
        "tv",
        "switch1",
        "tv1",
        "switch2",
        "tv2",
    ]
