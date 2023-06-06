def check_return_iterable(obj):
    if isinstance(obj, dict):
        return [obj]
    try:
        iter(obj)
        return obj
    except:
        return [obj]


def scale_charges(charges, n_particles):
    net_charge = sum(charges)
    abs_charge = sum([abs(charge) for charge in charges])
    adjust = abs(net_charge) / n_particles
    scaled_charges = []
    for idx, charge in enumerate(charges):
        new_charge = charge - (abs(charge) * (net_charge/abs_charge))
        scaled_charges.append(new_charge)
    return scaled_charges