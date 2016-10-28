# This file is only included as an example. Remove this file when you are
# ready to develop your plugin.
import os
import os.path
import pkg_resources

import pandas as pd
import q2templates


TEMPLATES = pkg_resources.resource_filename(
    "{{cookiecutter.package_name}}", 'assets')


def mapping_viz(output_dir: str, mapping1: dict, mapping2: dict,
                key_label: str, value_label: str) -> None:
    df1 = _dict_to_dataframe(mapping1, key_label, value_label)
    df2 = _dict_to_dataframe(mapping2, key_label, value_label)

    index = os.path.join(TEMPLATES, 'index.html')
    context = {
        "mapping1": df1.to_html(index=False, classes='dummy-class'),
        "mapping2": df2.to_html(index=False, classes='dummy-class')
    }

    q2templates.render(index, output_dir, context=context)


def _dict_to_dataframe(dict_, key_label, value_label):
    return pd.DataFrame(sorted(dict_.items()),
                        columns=[key_label, value_label])
