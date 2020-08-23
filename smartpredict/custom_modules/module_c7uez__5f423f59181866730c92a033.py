# ---------------------------------------------------
# Your import statements can be written here.
# All builtins python package can be imported.
# Popular libraries for ML like tensorflow, sklearn,
# pandas, nltk are also supported

# import tensorflow as tf
# import time
# other imports
# ---------------------------------------------------


class MyCustomModule:
    """A custom module class must contain "CustomModule" in its name."""

    #: This dictionary holds the property of your custom module
    p = {
        # Input specification, the keys of the dict are the inputs' name
        'in': {
            'input_1': {
                # Type of input data.
                'type': 'any',

                # Shown name.
                'name': 'Input 1',

                'order': 1,

                # Short description.
                'description': 'Default Input'
            }
        },

        # Output specification, the keys of the dict are the outputs' name
        'out': {
            'output_1': {
                # Type of output data.
                'type': 'any',

                # Shown name.
                'name': 'Output 1',

                'order': 1,

                # Short description.
                'description': 'Default Output'
            }
        },

        # Params specification, the keys of the dict are the name of the param.
        'params': {
            'param_1': {
                'label': 'Default Param',
                'type': 'str',
                'default': '',
                'input-type': 'text'
            }
        },

        # Other description of the module.
        'doc': {
            'author': 'John Doe',
            'framework': 'tensorflow, sk-learn',
            'description': 'lorem ipsum dolor sit amet.'
        },

        # Version.
        'version': '0.0'
    }

    def load(self):
        """Use this method to load your module.

        Load models, init objects, libraries..."""

    def run(self):
        """This method is called to run your module,

        Get input, read params, process data, set output."""

        # How to retrieve your input data.
        input_1_data = self.in_data['input_1']

        # How to retrieve your params value.
        param_1 = self.param['param_1']

        # How to process data.
        # Just write any number of methods you want and use them here.
        sample_out_data = self.sample_method(input_1_data, param_1)

        # Go to the definition of this method to see how to log.
        self.demo_log()

        # This is how to set output data.
        self.out_data['output_1'] = sample_out_data

    def sample_method(self, data, param):
        # This is an example of processing the data and producing the output
        self.logger.debug('Using the method.')
        sample_result = {
            'data': data,
            'param': param
        }
        return sample_result

    def demo_log(self):
        """You can use the `logger` property like any Logger created
        from python builtin logging module."""
        self.logger.debug('This is a debug log.')
        self.logger.info(self.name)
        self.logger.warning(self.doc)
