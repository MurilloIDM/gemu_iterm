def get_summary(data=[]):
    banks_summary = {}
    banks_list = set([moviment["bank"] for moviment in data])

    for bank in banks_list:
        total_input = sum([moviment['value']
                          for moviment in data if moviment['bank'] == bank and moviment['type'] == 'ENTRADA'])
        total_output = sum([moviment['value']
                            for moviment in data if moviment['bank'] == bank and moviment['type'] == 'SAÍDA'])
        resulting = total_input - total_output

        banks_summary[bank] = {'input': total_input, 'output': total_output, 'resulting': resulting}

    return banks_summary
