from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_db
from api.crud import ProjectCRUD, LogCRUD
from api.schemas import ProjectCreate, ProjectResponse, ProjectList, ProjectDetail
from typing import List
from uuid import UUID
import zipfile
import os
import tempfile
from fastapi.responses import FileResponse
from utils.logger import db_logger

router = APIRouter()

@router.post("/create-startup", response_model=ProjectResponse)
async def create_startup(
    project: ProjectCreate,
    db: AsyncSession = Depends(get_db)
):
    """Créer un nouveau projet startup après CEO, CTO, Dev, Marketing"""
    try:
        db_project = await ProjectCRUD.create(db, project)
        
        # Log the creation
        await db_logger.log_to_db(
            db_project.id, 
            f"Startup créée avec l'idée: {project.idea}"
        )
        
        return db_project
    except Exception as e:
        db_logger.error(f"Erreur lors de la création du projet: {e}")
        raise HTTPException(status_code=500, detail="Erreur lors de la création du projet")

@router.get("/projects", response_model=List[ProjectList])
async def get_projects(db: AsyncSession = Depends(get_db)):
    """Récupérer la liste de tous les projets"""
    try:
        projects = await ProjectCRUD.get_all(db)
        return projects
    except Exception as e:
        db_logger.error(f"Erreur lors de la récupération des projets: {e}")
        raise HTTPException(status_code=500, detail="Erreur lors de la récupération des projets")

@router.get("/projects/{project_id}", response_model=ProjectDetail)
async def get_project(
    project_id: UUID,
    db: AsyncSession = Depends(get_db)
):
    """Récupérer les détails d'un projet (roadmap + stack + metadata)"""
    try:
        project = await ProjectCRUD.get_by_id(db, project_id)
        if not project:
            raise HTTPException(status_code=404, detail="Projet non trouvé")
        return project
    except HTTPException:
        raise
    except Exception as e:
        db_logger.error(f"Erreur lors de la récupération du projet {project_id}: {e}")
        raise HTTPException(status_code=500, detail="Erreur lors de la récupération du projet")

@router.get("/projects/{project_id}/download")
async def download_project(
    project_id: UUID,
    db: AsyncSession = Depends(get_db)
):
    """Télécharger le code généré d'un projet en ZIP"""
    try:
        project = await ProjectCRUD.get_by_id(db, project_id)
        if not project:
            raise HTTPException(status_code=404, detail="Projet non trouvé")
        
        if not project.path or not os.path.exists(project.path):
            raise HTTPException(status_code=404, detail="Code généré non trouvé")
        
        # Create temporary ZIP file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.zip') as tmp_file:
            with zipfile.ZipFile(tmp_file.name, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(project.path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, project.path)
                        zipf.write(file_path, arcname)
            
            # Log the download
            await db_logger.log_to_db(
                project_id, 
                f"Code téléchargé pour le projet: {project.idea}"
            )
            
            # Return the ZIP file
            return FileResponse(
                tmp_file.name,
                media_type="application/zip",
                filename=f"project_{project_id}.zip"
            )
    
    except HTTPException:
        raise
    except Exception as e:
        db_logger.error(f"Erreur lors du téléchargement du projet {project_id}: {e}")
        raise HTTPException(status_code=500, detail="Erreur lors du téléchargement")