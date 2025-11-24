code = '''
import argparse
import torch
from tool.darknet2pytorch import Darknet

def export_to_onnx(cfg_file, weights_file, output_file, input_size=(416, 416)):
    print(f"Loading config from: {cfg_file}")
    model = Darknet(cfg_file)
    model.load_weights(weights_file)
    model.eval()

    print(f"Exporting to ONNX: {output_file}")
    dummy_input = torch.randn(1, 3, input_size[0], input_size[1])
    torch.onnx.export(model,
                      dummy_input,
                      output_file,
                      verbose=False,
                      opset_version=11,
                      input_names=['input'],
                      output_names=['output'])

    print(f"✅ Exported to: {output_file}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--cfg', required=True, help='Path to cfg file')
    parser.add_argument('--weights', required=True, help='Path to weights file')
    parser.add_argument('--output', required=True, help='Path to output ONNX file')
    parser.add_argument('--img-size', nargs=2, type=int, default=[416, 416], help='Input image size (h, w)')
    args = parser.parse_args()

    export_to_onnx(args.cfg, args.weights, args.output, tuple(args.img_size))
'''

with open("export_onnx.py", "w") as f:
    f.write(code)
