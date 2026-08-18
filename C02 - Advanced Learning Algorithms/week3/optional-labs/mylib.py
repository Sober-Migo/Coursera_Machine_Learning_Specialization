def pyls_definitions(config, document, position):
    settings = config.plugin_settings('jedi_definition')
    code_position = _utils.position_to_jedi_linecolumn(document, position)
    definitions = document.jedi_script().goto(
        follow_imports=settings.get('follow_imports', True),
        follow_builtin_imports=settings.get('follow_builtin_imports', True),
        **code_position)



def pyls_definitions(config, document, position):
    ...
    definitions = document.jedi_script(use_document_path=True).goto(
        follow_imports=settings.get('follow_imports', True),
        follow_builtin_imports=settings.get('follow_builtin_imports', True),
        **code_position)
    ...