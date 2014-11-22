{-# LANGUAGE ForeignFunctionInterface, TemplateHaskell #-}

module Export where
import Foreign.HaPy
import MyModule

initHaPy

-- Expose the factorial function
-- Remember to prepend single quote
pythonExport 'factorial
