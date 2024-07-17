from __future__ import annotations
from typing import cast

from ckan.common import CKANConfig
from ckan.lib.plugins import DefaultTranslation
from ckan.types import Schema
import ckan.plugins as p
import ckan.plugins.toolkit as tk


# import ckanext.reportview.cli as cli
# import ckanext.reportview.helpers as helpers
# import ckanext.reportview.views as views
# from ckanext.reportview.logic import (
#     action, auth, validators
# )

class ReportviewPlugin(p.SingletonPlugin, tk.DefaultDatasetForm,DefaultTranslation):
    p.implements(p.ITranslation)
    p.implements(p.IConfigurer)
    p.implements(p.IDatasetForm)
    def _modify_package_schema(self, schema: Schema) -> Schema:
        # Add our resource_report_id_text metadata field to the schema
        cast(Schema, schema['resources']).update({
                'resource_report_id_text' : [ tk.get_validator('ignore_missing') ]
                })
        return schema

    def create_package_schema(self):
        schema: Schema = super(
            ReportviewPlugin, self).create_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def update_package_schema(self):
        schema: Schema = super(
            ReportviewPlugin, self).update_package_schema()
        schema = self._modify_package_schema(schema)
        return schema
    def show_package_schema(self) -> Schema:
        schema: Schema = super(
            ReportviewPlugin, self).show_package_schema()
        schema = self._modify_package_schema(schema)
        cast(Schema, schema['resources']).update({
                'custom_resource_text' : [ tk.get_validator('ignore_missing') ]
            })
        return schema
    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self) -> list[str]:
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []
    # IConfigurer

    def update_config(self, config: CKANConfig):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        tk.add_template_directory(config, 'templates')

    
    # IAuthFunctions

    # def get_auth_functions(self):
    #     return auth.get_auth_functions()

    # IActions

    # def get_actions(self):
    #     return action.get_actions()

    # IBlueprint

    # def get_blueprint(self):
    #     return views.get_blueprints()

    # IClick

    # def get_commands(self):
    #     return cli.get_commands()

    # ITemplateHelpers

    # def get_helpers(self):
    #     return helpers.get_helpers()

    # IValidators

    # def get_validators(self):
    #     return validators.get_validators()
    
