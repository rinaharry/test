# ---------------------------------------------------- IMPORTS ---------------------------------------------------------
# Your import statements can be written here.
# All builtins python package can be imported.
# Popular libraries for ML like tensorflow, sklearn,
# pandas, nltk are also supported.
# ----------------------------------------------------------------------------------------------------------------------


# ------------------------------------------------- CONFIGURATION ------------------------------------------------------
# Follow this convention when specifying the configuration of your module.
# The name of each input and output are up to you, but the structure of each one of them should be the same.
from logging import Logger

configuration = {
    # You can create as many inputs as you want.
    'in': {
        'input_1': {
            'label': 'Input 1',
            'type': 'int',
            'order': 1,
            'description': 'This is the first input.',
        },
        'input_2': {
            'label': 'Input 2',
            'type': 'int',
            'order': 2,
            'description': 'This is the second input.',
        },
    },

    # You can also create as many outputs as you want
    'out': {
        'result': {
            'label': 'Result of the operation',
            'type': 'int',
            'order': 1,
            'description': 'This is the result of the operation.',
        }
    },

    # The parameters are shown when double-clicking the module or using the menu on its right while in edit mode.
    'params': {
        # Read the documentation for more details on the kind of parameters and options available in SmartPredict.
        'operation': {
            'label': 'Operation',
            'type': 'str',
            'default': 'Addition',
            'choices': ['Addition', 'Subtraction', 'Multiplication', 'Division'],
            'category': 'basic',
            'input-type': 'drop-down',
            'description': 'Choose the operation to be done.'
        }
    }
}


# ----------------------------------------------------------------------------------------------------------------------

# -------------------------------------------- CUSTOM MODULE FUNCTION --------------------------------------------------

# This is a normalized function, it must take "in_data" , "param", "logger" as parameters.
# The name of this function should also contain "custom_module" in it.
def custom_module_function(in_data: dict, param: dict, logger: Logger) -> dict:
    # Retrieve the input, and the parameters of the module as follows :
    first_number = in_data['input_1']
    second_number = in_data['input_2']
    operation = param['operation']
    logger.debug('Computing the operation...')

    # Create the logic of the custom module, this is just an example.
    result_switcher = {
        'Addition': first_number + second_number,
        'Subtraction': first_number - second_number,
        'Multiplication': first_number * second_number,
        'Division': first_number / second_number
    }
    result = result_switcher[operation]
    logger.debug('Finished computing the operation.')
    logger.info('Hey, this is the result : {} '.format(result))

    # The output of your function must be an "out_data" mapping dictionary, each key is as specified in configuration
    out_data = {
        'result': result,
    }

    # Return this map of output data
    return out_data
# ----------------------------------------------------------------------------------------------------------------------
