#!/usr/bin/python3

import zmq

import configuration


def request_set_light_levels(control_data):
    zmq_client = zmq.Context().socket(zmq.REQ)
    zmq_client.connect(configuration.transfer_protocol)
    zmq_client.send_pyobj(control_data)


if __name__ == '__main__':
    pwm_duty_cycles = configuration.dimmers_off

    while True:
        try:
            for room in pwm_duty_cycles.keys():
                pwm_duty_cycles[room] = float(input("Set light level in room %s to: " % room))
                if pwm_duty_cycles[room] < 0 or pwm_duty_cycles[room] > 100:
                    raise ValueError("Light level should be <0:100>, got %d instead." % pwm_duty_cycles[room])
            request_set_light_levels(pwm_duty_cycles)
        except ValueError as e:
            print("\n%s\n" % e)
        except KeyboardInterrupt:
            print("\nShutting down...\n")
            break
