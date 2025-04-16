from pathlib import Path
from obj2mjcf.mjcf_builder import MJCFBuilder
from obj2mjcf.material import Material
import trimesh

# 假设以下是你的输入
obj_filename = Path("tests/groups.obj")
work_dir = Path("tests/convex_decomp")

# 加载原始网格（用于可视化目的）
mesh = trimesh.load(obj_filename)

# 创建MJCF构建器
builder = MJCFBuilder(
    filename=obj_filename,
    mesh=mesh,
    materials=[],
    work_dir=work_dir,
    decomp_success=True
)

# 构建MJCF模型（可选参数add_free_joint用于添加自由关节）
builder.build(add_free_joint=False)

# 编译检查模型（可选）
builder.compile_model()

# 保存MJCF文件
builder.save_mjcf()