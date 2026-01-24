"""Initial migrations for users."""
from django.db import migrations, models
import django.utils.timezone

import apps.users.models


class Migration(migrations.Migration):
    """Create user model."""

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("jurisdictions", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("last_login", models.DateTimeField(blank=True, null=True, verbose_name="last login")),
                ("is_superuser", models.BooleanField(default=False, help_text="Designates that this user has all permissions without explicitly assigning them.", verbose_name="superuser status")),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("preferred_language", models.CharField(blank=True, max_length=10, null=True)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("groups", models.ManyToManyField(blank=True, help_text="The groups this user belongs to.", related_name="user_set", related_query_name="user", to="auth.group", verbose_name="groups")),
                ("user_permissions", models.ManyToManyField(blank=True, help_text="Specific permissions for this user.", related_name="user_set", related_query_name="user", to="auth.permission", verbose_name="user permissions")),
                (
                    "preferred_jurisdiction",
                    models.ForeignKey(blank=True, null=True, on_delete=models.PROTECT, related_name="users", to="jurisdictions.jurisdiction"),
                ),
            ],
            options={
                "abstract": False,
            },
            managers=[("objects", apps.users.models.UserManager()),],
        ),
    ]
