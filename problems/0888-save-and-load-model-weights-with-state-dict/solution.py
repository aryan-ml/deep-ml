import io
import torch
import torch.nn as nn

def copy_weights(src: nn.Module, dst: nn.Module) -> nn.Module:
    # TODO: serialize src's state dict into a buffer, rewind, then load it into dst
    
    buffer = io.BytesIO() ## This is like a fake file in RAM or a in memory file 

    state = src.state_dict()        ## Save the state dict of the src into state

    torch.save(state, buffer)       ## save the same thing into buffer file that we created 
    buffer.seek(0)                  ## Make sure the keep the pointer in front do that torch and load it properly

    state = torch.load(buffer)      ## Load the dict into state 
    dst.load_state_dict(state)      ## Load the same thing into new model behaves like wieghts and bias copy 

    return dst
