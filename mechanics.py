from config import SPEED_INCREMENT, SPEED_DECREMENT, BASE_SPEED, \
                   STEERING_STEP, MAX_NUM_CARS


def update_state(key, state):
    # respond to keys
    if key == ord('w'):
        state['speed'] += SPEED_INCREMENT
        state['speed'] = min(99, state['speed'])
    elif key == ord('s'):
        state['speed'] -= SPEED_DECREMENT
        state['speed'] = max(BASE_SPEED, state['speed'])
    elif key == ord('d'):
        state['car_x'] += STEERING_STEP
        state['car_x'] = min(1, state['car_x'])
    elif key == ord('a'):
        state['car_x'] -= STEERING_STEP
        state['car_x'] = max(-1, state['car_x'])
    elif key == -1:
        pass

    # update other cars
    if len(state['cars']) < MAX_NUM_CARS:
        pass
        # TODO: game['cars'] ....
